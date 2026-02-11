from django.urls import path,include
from .views import *
urlpatterns = [
    path('', home, name="home"),
    
    #Arguments
    path('good/<int:pk>', good_page ,name='good_page'),

]