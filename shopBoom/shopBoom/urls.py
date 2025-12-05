from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path,include
#from users.views import login_user 

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', login_user, name="login"),
    path('', include('users.urls')),
    path('users/', include('users.urls')),
    path('prometheus/', include('django_prometheus.urls')),    

    
    #path('auth/', include("django.contrib.auth.urls")) не нужен
    #path('cart', include('cart.url')) add later
]

#if settings.Debug:
 #   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
