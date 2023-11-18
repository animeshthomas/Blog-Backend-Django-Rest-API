from django.contrib import admin
from django.urls import path,include
from .import views


urlpatterns = [
    path('addblog/',views.addBlog,name='addblog'),
    path('viewblog/',views.view_blog,name='viewblog'),
    path('mypost/',views.ViewMypost,name='mypost'),
]