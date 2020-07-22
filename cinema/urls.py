from django.contrib import admin
from django.urls import path, include
from peliculas import views

urlpatterns = [
    #path('', views.home),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('users/', include(('users.urls', 'users'), namespace='users')),
]
