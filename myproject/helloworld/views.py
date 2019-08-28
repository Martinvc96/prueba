from django.shortcuts import render
from django.http import HttpResponse

def hello(reques):
    return HttpResponse("Hello World!")