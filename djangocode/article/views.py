from django.shortcuts import render, redirect
from article.models import *

def index(request):
  articles = Article.objects.all()
  return render(request, 'article/index.html', locals())

def new(request):
  return render(request, 'article/new.html', locals())

def create(request):
  article = Article(title=request.POST.get('title'), content=request.POST.get('content'))
  article.save()
  return redirect('/')