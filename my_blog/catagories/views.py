from django.shortcuts import render, redirect
from .models import Catagory

# Create your views here.
def catagories_list(request):
    catagories = Catagory.objects.order_by('name')
    return render(request, 'catagories/catagories.html', {
        'catagories' : catagories
    })