from django.urls import path ,include
from . import views

from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('mydayviewset',views.MydayViewSet,basename='myday-viewset')
router.register('importantviewset',views.ImportantViewSet,basename='important-viewset')
router.register('planviewset',views.PlanViewSet,basename='plan-viewset')
router.register('playlistviewset',views.PlayListViewSet,basename='playlist-viewset')



urlpatterns = [

    path('',views.Home,name='home-api'),
    path('viewset/',include(router.urls)),
    path('<str:playlist>/',views.PlayListApi,name='playlist-api'),
    path('<str:playlist>/?title=<str:title>',views.PlayListApi,name='search'),
    path('<str:playlist>/all/',views.views_all,name='all'),
    path('<str:playlist>/create/',views.create,name='create'),
    path('<str:playlist>/update/', views.Update, name='update'),
    path('<str:playlist>/delete/',views.delete,name='update'),
]
