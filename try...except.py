#try bloğu, bir kod bloğunu hatalara karşı test etmenizi sağlar.

#except bloğu, hatayı işlemenizi sağlar.

#else bloğu, herhangi bir hata olmadığında kod yürütmenizi sağlar.

#finally bloğu, try- ve except bloklarının sonucundan bağımsız olarak kod yürütmenize olanak tanır
"""
#x tanımlı değil o yüzden except deki print ekrana yazdırılır
try:
  print(x)
except:
  print("An exception occurred")
"""
#try bloğu olmadan, program çöker ve bir hata verir:


#kodu normal çalıştırdığımızda nameError hatası vereceği için except
#nameErrordaki printi yazdırdı
"""
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

#Herhangi bir hata oluşmadıysa yürütülecek bir kod bloğunu tanımlamak için else anahtar sözcüğünü kullanabilirsiniz:
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")


#finally bloğu, belirtilirse, try bloğunun bir hata verip vermediğine bakılmaksızın yürütülür
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")


#bir dosya açılmaya çalışıldı ama dosya olmadığı için except printi yazdırıldı
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")  


#Python geliştiricisi olarak, bir koşul oluşursa bir istisna atmayı seçebilirsiniz.
#Bir istisna oluşturmak (veya yükseltmek) için raise anahtar sözcüğünü kullanın.

x = -1
#-1<0 olduğu için raise çıktısı verdi
if x < 0:
  raise Exception("Sorry, no numbers below zero")


#raise anahtar sözcüğü bir istisna oluşturmak için kullanılır.
#Ne tür bir hatanın tetikleneceğini ve kullanıcıya yazdırılacak metni tanımlayabilirsiniz.

x =("hello world")

if not type(x) is int:
  raise TypeError("Only integers are allowed")

"""