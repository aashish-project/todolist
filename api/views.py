# apis
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, redirect
from rest_framework import serializers,viewsets,status
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


from .serializer import *
from todo.models import *

class MydayViewSet(viewsets.ModelViewSet):
    queryset = MyDayClass.objects.all()
    serializer_class = MyDaySerializer
    def create(self, request, *args, **kwargs):
        if request.user:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            playlist_data = serializer.validated_data.get('playlist')
            finished_data = serializer.validated_data.get('finished')
            user=serializer.validated_data.get('user')
            # Create the Playlist object
            playlist = None
            if playlist_data:
                playlist = TodoClass.objects.create(**playlist_data)
            # Create the Finished object
            finished = None
            if finished_data:
                finished = FinishTimeClass.objects.create(**finished_data)

            # Create the PlayListClass object
            play_list = MyDayClass.objects.create(playlist=playlist,user=user)

            serializer.instance = play_list
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class ImportantViewSet(viewsets.ModelViewSet):
    queryset = ImportantClass.objects.all()
    serializer_class = ImportantSerializer

    def create(self, request, *args, **kwargs):
        if request.user:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            playlist_data = serializer.validated_data.get('playlist')
            finished_data = serializer.validated_data.get('finished')
            user=serializer.validated_data.get('user')
            # Create the Playlist object
            playlist = None
            if playlist_data:
                playlist = TodoClass.objects.create(**playlist_data)
            # Create the Finished object
            finished = None
            if finished_data:
                finished = FinishTimeClass.objects.create(**finished_data)

            # Create the PlayListClass object
            play_list = ImportantClass.objects.create(playlist=playlist,user=user)

            serializer.instance = play_list
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class PlanViewSet(viewsets.ModelViewSet):
    queryset = PlanClass.objects.all()
    serializer_class = PlanSerializer

    def create(self, request, *args, **kwargs):
        if request.user:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            playlist_data = serializer.validated_data.get('playlist')
            finished_data = serializer.validated_data.get('finished')
            user=serializer.validated_data.get('user')
            # Create the Playlist object
            playlist = None
            if playlist_data:
                playlist = TodoClass.objects.create(**playlist_data)
            # Create the Finished object
            finished = None
            if finished_data:
                finished = FinishTimeClass.objects.create(**finished_data)

            # Create the PlayListClass object
            play_list = PlanClass.objects.create(playlist=playlist,user=user,finished=finished)

            serializer.instance = play_list
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class PlayListViewSet(viewsets.ModelViewSet):
    queryset = PlayListClass.objects.all()
    serializer_class = PlaylistSerializer

    def create(self, request, *args, **kwargs):
        if request.user:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            playlist_data = serializer.validated_data.get('playlist')
            finished_data = serializer.validated_data.get('finished')
            user=serializer.validated_data.get('user')
            # Create the Playlist object
            playlist = None
            if playlist_data:
                playlist = TodoClass.objects.create(**playlist_data)
            # Create the Finished object
            finished = None
            if finished_data:
                finished = FinishTimeClass.objects.create(**finished_data)

            # Create the PlayListClass object
            play_list = PlayListClass.objects.create(playlist=playlist,user=user,finished=finished)

            serializer.instance = play_list
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

@api_view(['GET'])
def Home(request):
    api_url = {
        'myday': 'myday',
        'important': 'important',
        'plan': 'plan',
        'playlist': 'playlist',
    }
    formatted_url = {}
    for key, value in api_url.items():
        formatted_url[key] = request.build_absolute_uri('/api/'+value)
    return Response(formatted_url)


@api_view(['GET'])
def PlayListApi(request, playlist):
    title=request.GET.get('title')
    print(title)
    if title:
        if playlist == 'myday':
            items = MyDayClass.objects.filter(playlist__title=title)
            serializer = MyDaySerializer(items, many=True)
        elif playlist == 'important':
            items = ImportantClass.objects.filter(playlist__title=title)
            serializer = ImportantSerializer(items, many=True)
        elif playlist == 'plan':
            items = PlanClass.objects.filter(playlist__title=title)
            serializer = PlanSerializer(items, many=True)
        else:
            items = PlayListClass.objects.filter(playlist__title=title)
            serializer = PlaylistSerializer(items, many=True)
        return Response(serializer.data)

    api_url = {
        'home': '',
        'all_items': 'all',
        'Search by title': '?title=',
        'Add': 'create',
        'Update': 'update/?pk=',
        'Delete': 'delete/?pk='
    }

    formatted_urls = {}
    for key, value in api_url.items():
        formatted_urls[key] = request.build_absolute_uri(
            f'/api/{playlist}/'+value)
    return Response(formatted_urls)


@api_view(['GET'])
def views_all(request, playlist):
    if playlist == 'myday':
        items = MyDayClass.objects.all()
        serializer = MyDaySerializer(items, many=True)
    elif playlist == 'important':
        items = ImportantClass.objects.all()
        serializer = ImportantSerializer(items, many=True)
    elif playlist == 'plan':
        items = PlanClass.objects.all()
        serializer = PlanSerializer(items, many=True)
    else:
        items = PlayListClass.objects.all()
        serializer = PlaylistSerializer(items, many=True)
    return Response(serializer.data)


# @api_view(['POST'])
def create(request, playlist):
    if playlist == 'myday':
        return redirect('/api/viewset/mydayviewset/')
    elif playlist == 'important':
        return redirect('/api/viewset/importantviewset/')
    elif playlist == 'plan':
        return redirect('/api/viewset/planviewset/')
    else:
        return redirect('/api/viewset/playlistviewset/')


@api_view(['GET', 'POST'])
def Update(request, playlist):
    pk=request.GET.get('pk')
    if pk:
        if playlist == 'myday':
            item = MyDayClass.objects.filter(id=pk)
            value=MyDaySerializer(item,many=True)
            serializer = MyDaySerializer(item, data=request.data)

        elif playlist == 'important':
            item = ImportantClass.objects.filter(id=pk)
            value=ImportantSerializer(item,many=True)
            serializer = ImportantSerializer(item, data=request.data)

        elif playlist == 'plan':
            item = PlanClass.objects.filter(id=pk)
            value=PlanSerializer(item,many=True)
            serializer = PlanSerializer(item, data=request.data)

        else:
            item = PlayListClass.objects.filter(id=pk)

            value=PlaylistSerializer(item,many=True)

            serializer = PlaylistSerializer(item, data=request.data)

        if request.method == 'POST':
            if serializer.is_valid():
                serializer.save() 
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        
        return Response(value.data)
    else:
        return views_all(request._request,playlist)

@api_view(['DELETE'])
def delete(request,playlist):
    pk=request.GET.get('pk')
    if playlist=='myday':
        Item=MyDayClass
    elif playlist=='plan':
        Item=PlanClass
    elif playlist == 'important':
        Item=ImportantClass
    else:
        Item=PlayListClass
    item = get_object_or_404(Item, id=pk)
    if item.playlist:
        playlist=item.playlist
        # print(playlist)
        playlist.delete()
    if item.finished:
        finished=item.finished
        # print(finished)
        finished.delete()
    # print(item)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)