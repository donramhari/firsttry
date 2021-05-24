from django.shortcuts import render
from django.views.generic import TemplateView
from . models import Post




def index(request):
    return render(request, 'index.html', context = { "posts":Post.objects.all} )

def blog_list(request):
    return render(request, 'try.html', context = { "posts":Post.objects.all} )