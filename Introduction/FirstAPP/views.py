from django.shortcuts import render
from .models import ChaiVarity
from django.shortcuts import get_object_or_404

# Create your views here.
def all_FirstAPP(request):
    chais = ChaiVarity.objects.all()
    return render(request,'FirstAPP/all_FirstAPP.html', {'chais':chais} )

def chai_details(request,chai_id):
    chai = get_object_or_404(ChaiVarity,pk=chai_id)
    return render(request,'FirstAPP/chai_details.html', {'chai':chai} )

def chai_price(request,chai_id):
    chai_price = get_object_or_404(ChaiVarity,pk=chai_id)
    return render(request,'FirstAPP/chai_details.html',{'chai_price':chai_price})

def chai_store_view(request):
    return render(request,'FirstAPP/chai_store.html')