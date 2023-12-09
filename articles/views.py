from django.shortcuts import render
from . import models

def list(request):
    articles=models.Articles.objects.all()
    arg={'articles':articles}
    return render(request,'articles/list.html',arg)