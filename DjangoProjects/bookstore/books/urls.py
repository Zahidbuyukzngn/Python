from django.urls import path
from . import views

#Bu kod, projede ana sayfa (kök URL) için bir URL yönlendirmesi tanımlar.
#Kök URL'ye gidildiğinde, views.py dosyasındaki index işlevi çalıştırılır.
urlpatterns = [
    path('',views.index,name='index')
]

