from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout,login
from django.db.models import BooleanField, Case, When
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.db.models import Q

from .forms import *
from datetime import date


current_date = date.today()
template_name='home.html'


@login_required
def combined_function(request, playlist):
    user=request.user
    time = False
    ctr = None
    heading = set()

    play = PlayListClass.objects.filter(user=user).order_by('title')
    for lst in play:
        heading.add(lst.title)
    tasks = {}

    if playlist == 'myday':
        playlists = MyDayClass.objects.filter(user=user, playlist__create_time__date=current_date).order_by(Case(When(playlist__finished=False, then=0), default=1),'-playlist__create_time')
        ctr = MyDayClass
    elif playlist == 'important':
        playlists = ImportantClass.objects.filter(user=user).order_by(Case(When(playlist__finished=False, then=0), default=1),'-playlist__create_time')
        ctr = ImportantClass
    elif playlist == 'plan':
        playlists = PlanClass.objects.filter(user=user).order_by(Case(When(playlist__finished=False, then=0), default=1),'-playlist__create_time')
        ctr = PlanClass
        time = True
    else:
        playlists = PlayListClass.objects.filter(Q(title=playlist.lower()) & Q(user=user)).order_by(Case(When(playlist__finished=False, then=0), default=1),'-playlist__create_time')
        ctr = PlayListClass
        time = True

    for ptr in playlists:
        if ptr.finished:
            if ptr.finished.finish_time < timezone.now():
                ptr.playlist.finished = True
                ptr.playlist.save()
                ptr.save()
            tasks[ptr.playlist] = ptr.finished
        else:
            if ptr.playlist!=None and ptr.playlist.create_time.date() < timezone.now().date():
                ptr.playlist.finished = True
                ptr.playlist.save()
                ptr.save()
            tasks[ptr.playlist] = None

    if request.method == "POST":
        form3=NewPlayListForm(request.POST)
        form1 = TodoForm(request.POST)
        
        if form3.is_valid() and form3.cleaned_data.get('form_type') == 'form3':
            var=form3.save()
            var.user=user
            var.save()
            return redirect('todo',playlist=playlist)
        form2 = None
        if time:
            form2 = FinishTimeForm(request.POST)
        
        if form1.is_valid() and form1.cleaned_data.get('form_type') == 'form1':
            todo = form1.save()
        if form2 is not None and form2.is_valid():
            finish = form2.save()
        if ctr == PlayListClass:
            ctr, _ = PlayListClass.objects.get_or_create(title=playlist,user=user, playlist=todo, finished=finish)
        elif time:
            ctr, _ = ctr.objects.get_or_create(playlist=todo, finished=finish,user=user)
        else:
            ctr, _ = ctr.objects.get_or_create(playlist=todo,user=user)
        return redirect('todo', playlist=playlist)
    else:
        form1 = TodoForm()
        form2 = None
        if time:
            form2 = FinishTimeForm()
        form3=NewPlayListForm()

    if tasks!={None:None}:
        valid=True
    else:
        valid=False
    context = {
        'tasks': tasks,
        'headings': heading,
        'form1': form1,
        'form2': form2,
        'form3':form3,
        "list":valid,
        "playlist": playlist,
        "path":str(playlist),
    }
    print('/'+str(playlist)+'/')
    return render(request, template_name, context)




@login_required
def delete(request,playlist,uuid):
    user=request.user
    time=False
    if playlist=='myday':
        obj=MyDayClass.objects
    elif playlist=='important':
        obj=ImportantClass.objects
    elif playlist=='plan':
        obj=PlanClass.objects
        time=True
    else:
        obj=PlayListClass.objects
        time=True


    if obj :
        todo=TodoClass.objects.get(pk=uuid)
        play=obj.get(playlist=todo)
        if(obj.get(playlist=todo).user==user):
            if time:
                finish=play.finished
                finish.delete()
            
            play.delete()
            todo.delete()
            return redirect('todo',playlist=playlist)
        return HttpResponse("Permission Denied")
    return HttpResponse('Unable to find data')
        
        
@login_required
def star(request, playlist, uuid):
    user = request.user
    todo = TodoClass.objects.get(id=uuid)

    if playlist == 'myday':
        play = todo.mydayclass_set
    elif playlist == 'plan':
        play = todo.planclass_set
    elif playlist == 'important':
        play = todo.importantclass_set
    else:
        play = todo.playlistclass_set

    if not play.exclude(user=user).exists():
        todo.star = not todo.star
        todo.save()
        return redirect('todo', playlist=playlist)

    
@login_required
def finish_task(request, playlist, uuid):
    user = request.user
    todo = TodoClass.objects.get(id=uuid)

    if playlist == 'myday':
        related_manager = todo.mydayclass_set
    elif playlist == 'plan':
        related_manager = todo.planclass_set
    elif playlist == 'important':
        related_manager = todo.importantclass_set
    else:
        related_manager = todo.playlistclass_set

    if not related_manager.exclude(user=user).exists():
        todo.finished = not todo.finished
        todo.save()
        # print(var)
        return redirect('todo', playlist=playlist)


@login_required
def user_form(request):
    if User.objects.filter(username=request.user.username).exists():
        return redirect('todo','myday')
    if request.method == "POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print('get saved')
            return redirect('user-create')
    else:
        form=UserCreationForm()
    # print(form)
    return render(request,'user-creation-form.html',{'form':form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('todo',playlist='myday')  # Replace 'home' with the name of your home URL pattern
    else:
        form = UserCreationForm()
    return render(request, 'login_register.html', {'form': form})


def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    print(request.user)
    return redirect('login')