from django.urls import path

from . import views

urlpatterns = [
    path('innerpg.html', views.innerpg, name='index'),
    # path('innerpg', views.innerpg, name='index'),
    path('',views.new,name='new'),
    # path('innerpg',views.i)
    path('appStart',views.appStart,name='appStart'),
    path('appStart1',views.appStart1,name='appStart1'),
]