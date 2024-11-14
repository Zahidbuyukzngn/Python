from django.shortcuts import render
from django.http import HttpResponse

"kullanıcıya gösterdiğimiz götüntü için kuralları yazdığımız kısımdır views.py"
# Create your views here.

#ekrana anasayfa yazdırdık
def index(request):
    return HttpResponse("Anasayfa")
