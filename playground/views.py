from django.http import HttpResponse
from django.shortcuts import render

def say_hello(request):
    return HttpResponse("Hello World")

def say_hello2(request):
    return render(request, 'hello.html',{'name':'Sundar'})