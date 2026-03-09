from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from users.views import index, inicio, register, acerca_de

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('index/', index, name='index'),
    path('inicio/', inicio, name='inicio'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('acerca-de/', acerca_de, name='acerca_de'),
]