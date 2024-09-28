#txt dosyasından sonra write ile belirttiğimiz cümle en sona eklendi "a"sayesinde
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

#"a" - Ekle - dosyanın sonuna eklenir

#"w" - Yaz - mevcut herhangi bir içeriğin üzerine yazar
#txt deki metni yazdırmadı hiç
f = open("demofile2.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("demofile2.txt", "r")
print(f.read())

"""
Python'da yeni bir dosya oluşturmak için aşağıdaki parametrelerden biriyle open() yöntemini kullanın:

"x" - Oluştur - bir dosya oluşturur, dosya varsa bir hata döndürür

"a" - Ekle - belirtilen dosya yoksa bir dosya oluşturur

"w" - Write - belirtilen dosya yoksa bir dosya oluşturur

"""
#deneme.txt adında dosya oluşturuldu
f = open("deneme.txt","x")


f = open("myfile.txt", "w")   # Dosya yoksa oluşturur
f.write("Hello World!")
f.close()