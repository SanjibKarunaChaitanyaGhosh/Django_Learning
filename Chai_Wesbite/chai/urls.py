from django.urls import path
from .import views

# localhost:8001/chai
# localhost:8001/chai/order
urlpatterns = [
    path('',views.all_chai, name='all_chai'),
    path('order',views.order, name='order'),
]