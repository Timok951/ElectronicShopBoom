from django.shortcuts import render
from .models import Good
from users.models import User

def home(request):
    goods = Good.objects.all()
    users = User.objects.all()

    return render(request, "main/home_page.html", {'Goods':goods, 'Users':users})

def good_page(request, pk):
    good = Good.objects.get(id=pk)
    users = User.objects.all()
    return render(request, 'good/good_page.html', {'Good':good, 'Users':users})

def category_page(requeest, pk):
    