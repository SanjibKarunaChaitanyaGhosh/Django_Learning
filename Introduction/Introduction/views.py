from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello guys Welcome to my Page")
    return render(request,'index.html')

def about(request):
    return HttpResponse("This is about page")

def contact(request):
    return HttpResponse("This is contact page")

