students={}
number=input("Ogrenci numarasını giriniz: ")
name=input("Ogrenci adını girin: ")
surname=input("ogrenci soyadını giriniz: ")
phone=input("ogrenci telefon numarasını giriniz: ")

#students sözlüğüne yeni bir öğe eklemek veya mevcut bir öğeyi güncellemek için kullanılır.
#update metodu, verilen sözlüğü students sözlüğüne ekler.
#döngüleri öğrenmediğimiz için bu şekilde 3 kere yaptık


students.update({
    number:{
    "ad":name,
    "soyad":surname,
    "telefon no":phone
    }
})
#students[number]= {
            #"adı":name,
            #"soyadı":surname,
            #"telefon numarası":phone
                  #}

number=input("Ogrenci numarasını giriniz: ")
name=input("Ogrenci adını girin: ")
surname=input("ogrenci soyadını giriniz: ")
phone=input("ogrenci telefon numarasını giriniz: ")

students.update({
    number:{
    "ad":name,
    "soyad":surname,
    "telefon no":phone
    }
})
     
number=input("Ogrenci numarasını giriniz: ")
name=input("Ogrenci adını girin: ")
surname=input("ogrenci soyadını giriniz: ")
phone=input("ogrenci telefon numarasını giriniz: ")

students.update({
    number:{
    "ad":name,
    "soyad":surname,
    "telefon no":phone
    }
})

print(students)

#eklenen öğrenciler içinden aranan öğrenciyi numara üzerinden bulamyı sağladık
print("*"*50)

ogrNo=input("Aradığınız öğrenci numarasını giriniz: ")
student=students[ogrNo]
print(student)