from django.http import HttpResponse
from django.shortcuts import render
# 2020.5.19
# Create your views here.

def index(request):
    return HttpResponse('hello World')