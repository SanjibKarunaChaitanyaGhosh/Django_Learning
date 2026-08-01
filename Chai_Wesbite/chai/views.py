from django.shortcuts import render
from .models import ChaiVarity

# Create your views here.
def all_chai(request):
    chais = ChaiVarity.objects.all()
    return render(request,'chai/all_chai.html',{'chais':chais})

def order(request):
    return render(request,'chai/order.html')