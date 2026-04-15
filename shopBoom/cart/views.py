from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from shop.models import Good
from .models import Order, OrderItem
from django.http import JsonResponse
from cart.services import Cart

def cart_summarry(request):
    return render(request, "cart/cart_summary.html", {} )

def cart_add(request, pk):
    pass

def cart_delete(request):
    pass

def cart_update(request):
    pass