from django.shortcuts import render, redirect
from .models import Catagory
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def catagories_list(request):
    catagories = Catagory.objects.order_by('name')
    return render(request, 'catagories/catagories.html', {
        'catagories' : catagories
    })