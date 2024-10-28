#başka bir projeyi başka bir projeye ekleme
#as ile kısaltma yaptık yapmasak da olurdu

# import functions as func
# func.greeting

#tüm içeriği * ile aktarabiliriz ama eğer büyük bir dosyaysa buna gerek yok
# from functions import *
# greeting()

#bu şekilde sadece istediğimiz fonksiyonu çağırabiliriz
from functions import greeting
greeting(first_name="mehmet", last_name="ak",age=22)