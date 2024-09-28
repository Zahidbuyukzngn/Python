#başka dosyadaki metne burdan erişebiliriz
f = open("regex.py", "r")

print(f.read())

#başka dosyalardan açma
#f = open("D:\\myfiles\welcome.txt", "r")

#print(f.read())

#sadece 5 karakter alır adını belirttiğimiz dosyadan
f = open("regex.py", "r")
print(f.read(5))

#sadece 1 tane satırı alır(ile satırı aldı)
f = open("regex.py", "r")
print(f.readline())
#readline() iki kez çağırarak, ilk iki satırı okuyabilirsiniz:

#dosyada satır satır dolaşma
f = open("sets.py", "r")
for x in f:
  print(x)


#dosyayı kapatma
f = open("sets.py", "r")
print(f.readline())
f.close()

#Not: Dosyalarınızı her zaman kapatmalısınız, bazı durumlarda arabelleğe alma nedeniyle bir dosyada yapılan değişiklikler siz dosyayı kapatana kadar gösterilmeyebilir.