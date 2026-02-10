from django.urls import path,include
from .views import *
urlpatterns = [
    path('', home, name="home"),
    path('good/<int:pk>', good_page ,name='good_page'),
    path('category/<str:foo>', category, name="category_page")

]