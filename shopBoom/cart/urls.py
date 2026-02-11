from django.urls import path,include
from .views import *

urlpatterns = [
    path('', cart_summarry, name="cart_summarry"),
    path('add/', cart_add, name='card_add'),
    path('delete/', cart_delete, name='cart_delete'),
    path('update/', cart_update, name='cart_update')
]