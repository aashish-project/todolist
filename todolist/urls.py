"""
URL configuration for todolist project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from todo.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',user_form,name='user-creation-form'),
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
    # path('accounts/',include('django.contrib.auth.urls')),
    path("accounts/login/", auth_views.LoginView.as_view(template_name='login_register.html'),name='login'),
    path('accounts/register/', register, name='register'),
    path('accounts/logout/', logout, name='logout'),
    # path('create-new-playlist/',CreateNewPlayListFunction,name='create-new-playlist'),
    
    path('<str:playlist>/',combined_function,name='todo'),
    path('<str:playlist>/delete/<uuid:uuid>',delete,name='delete-task'),
    path('<str:playlist>/star/<uuid:uuid>',star,name='star-task'),
    path('<str:playlist>/finish_task/<uuid:uuid>',finish_task,name='finish-task'),
    path('<str:playlist>/create-task',combined_function,name='create-task'),
]
