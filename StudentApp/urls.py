from django.contrib import admin
from django.urls import path, include

from StudentApp import views

urlpatterns = [
    path('',views.loginfun,name='login'),
    path('register',views.registerfun,name='register'),
    path('logout',views.logoutfun,name='logout'),
    path('home',views.home,name='home'),
    path('add/',views.add,name='add'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('delete/<int:id>',views.deletefun,name='delete'),
    path('dummy/',views.dummy,name='dummy')
]
