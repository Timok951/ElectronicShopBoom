from django.shortcuts import render
from .models import Good
def home(request):
    Goods = Good.objects.all()

    return render(request, "main/home_page.html", {'Goods':Goods})
