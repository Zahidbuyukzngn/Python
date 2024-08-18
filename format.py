Name="Ahmet"
Surname="Kızkaban"
age=19

#boşluklara .format ile gelmesi gereken değerleri verdik
print("My name is {} {} I'am {} years old".format(Name,Surname,age))

#burda değer vererek atadık,istediğimiz gibi yerlerini değiştirebiliriz
print("My name is {s} {n} I'am {a} years old".format(n=Name,s=Surname,a=age))

#{r:5.4} diyerek 0 ile önceki cümle arası boşluk kaç birim olacak onu söylüyoruz 5 dedik ama sayılar 5 birim olduğu için sola boşluk vermedi
#4 ile de . dan sonra kaç basamak olacağını belirtiyoruz
result=200/700
print("the result is {r:5.4}".format(r=result))

#en basit yöntemdir başa f koy ve parantez içine doldur
print(f"My name is {Name} {Surname} I'am {age} years old")