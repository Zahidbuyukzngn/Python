try:
 sayı1=int(input("bölmek istediğiniz ilk sayıyı girin: "))
 sayı2=int(input("bölmek istediğiniz ikinci sayıyı girin: "))
 result=sayı1/sayı2
 
#exceptlerin karşısına konsollarda verilen hataları yazarak uygulamanın hata almamasını sağladık.
#Python'da except bloğunda as e ifadesi, yakalanan istisnayı bir değişkene atamayı sağlar.
#Böylece hatanın detaylarını e değişkeni üzerinden inceleyebilirsiniz.
except ZeroDivisionError as e:
 print("Sıfıra bölünemez hata!",e)

except ValueError as e:
 print("Lütfen sadece rakam girin!",e)

except Exception as e:
 print("Bilinmeyen bir hata oluştu: ",e)

#exceptler çalışmazsa else ile sonuç yazdırırlır
else:
 print(result)

#program sonunda bu printi yazdırır
finally:
 print("this will alwasy execute")

