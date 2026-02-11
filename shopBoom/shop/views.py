from django.shortcuts import render, redirect
from .models import Good, Type, Tag, Company
from django.contrib import messages
from users.models import User
from .forms import *
from django.http import HttpResponse
from shop.filters import GoodFilter

def home(request):
    goods = Good.objects.all()
    users = User.objects.all()
    type = Type.objects.all()
    
    goodFilter = GoodFilter(request.GET,queryset=Good.objects.all() )

    context = {
        'Goods':goodFilter.qs, 
        'Users':users,
        'Types':type,
        'Form':goodFilter.form,
        }
    return render(request, "main/home_page.html", context)
    


def good_page(request, pk):
    good = Good.objects.get(id=pk)
    users = User.objects.all()
    context ={
        'Good':good, 
        'Users':users,
    }
    return render(request, 'good/good_page.html', context)

