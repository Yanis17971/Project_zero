
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('home.urls')),
    path('icecream/', include('icecream.urls')),
    path('admin/', admin.site.urls),
]
