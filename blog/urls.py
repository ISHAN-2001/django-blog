from django.contrib import admin
from django.urls import path , include
from  . import views

urlpatterns = [
    path('',views.home , name = 'blogHome'),
    path('<int:myid>',views.blogPost , name = 'blogPost')
]
