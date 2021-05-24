
from django.urls import path
from . import views

urlpatterns = [
   
    
    path('',views.index, name="temp"),
    path('bloglist', views.blog_list, name="blog"),
]