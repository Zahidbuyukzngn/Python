#dosyayı bulur ve siler
import os
os.remove("deneme.txt")

#dosyanın var olup olmadığını kontrol eder,varsa siler yoksa else ile dosya yok diye çıktı döner
import os

if os.path.exists("deneme.txt"):
    os.remove("deneme.txt")
else:
    print("the file doesn't exist")


#klasör silme
#Yalnızca boş klasörleri kaldırabiliriz.
import os 
os.rmdir("klasorun ismi")