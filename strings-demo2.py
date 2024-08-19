website="WWW.zahidbuyukzengin.com"
course="BTK eğitimleriyle severek Python öğreniyorum"

# ekstra- course dizisinde kaç karakter vardır

print(len(website))
# 1- course dizisinde kaç karakter vardır
print(len(course))
# 2-website içinden www karakterlerini alınız
print(website[ :3])
# 3-website içinden com karakterlerini alınız
print(website[21:24])
# 4- course içinden ilk 10 ve son 10 karakteri alınız
print(course[0:10])
print(course[-10:])

# 5-course değişkenindeki cümleyi tersten yazdırınız
print(course[::-1])


name,surname,age,job="Kadir","Karabacak",26,"student"

# 6- yukardaki verilen değişkenlerle aşağıdaki cümleyi yazdırınız
#benim adım kadir karabacak,yaşım 26 ve mesleğim öğrencilik
#my name is kadir karabacak,ı have 26 years old and my job is as a student
print(f"My name is {name} {surname},ı have {age} years old and my job is as a {job}")

# 7- hello world ifadesindeki w harfini büyük W yapınız
#replace metodu 
s="Hello world"
s= s.replace('w','W')
print(s)

# 8- 'abc' ifadesini arka arkaya 3 kere yazdırın
print(3*"abc ")





