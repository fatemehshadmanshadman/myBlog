from django.shortcuts import render
from . import models
from django.shortcuts import HttpResponse

def list(request):
    articles=models.Articles.objects.all()
    arg={'articles':articles}
    return render(request,'articles/list.html',arg)

def detail(request,slug):
    # return HttpResponse(slug)
    arti=models.Articles.objects.get(slug=slug)
    return render(request,'articles/detail.html',{'arti':arti})