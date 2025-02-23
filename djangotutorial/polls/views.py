from django.shortcuts import render

# Create your views here.
from django.http import response, HttpResponse


def index(request):
    return HttpResponse("你好，你处于投票界面！")