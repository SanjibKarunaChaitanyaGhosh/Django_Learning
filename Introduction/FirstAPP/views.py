from django.shortcuts import render
from .models import ChaiVarity

# Create your views here.
def all_FirstAPP(request):
    chais = ChaiVarity.objects.all()
    return render(request,'FirstAPP/all_FirstAPP.html',{'chais':chais})



# def order(request):
#     return render(request,'FirstAPP/all_FirstAPP.html')