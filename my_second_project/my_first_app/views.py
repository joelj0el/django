from django.shortcuts import render
from .models import Carro

def myView(request):
    
    car_list = [{'title': 'BMW'}, {'title': 'Mazda'}]    
    context = {'car_list': car_list}
    return render(request, 'my_sceond_app/car_list.html', context)
