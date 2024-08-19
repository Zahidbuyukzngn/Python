#Sözlükler değiştirilebilir; yani sözlük oluşturulduktan sonra öğeleri değiştirebilir,
#Ekleyebilir veya kaldırabiliriz.


#dictionary tanımlama key-value ilişkisi vardır sola key sağa value
'''
plakalar={"konya":42,"Ankara":6,"İstanbul":0}

print(plakalar["Ankara"])
print(plakalar["konya"])

plakalar["İstanbul"]=34
print(plakalar)
'''

users={"User1":{
       
    'roles':["User"],
    'age':19,
    'name':'Zahid',
    'phone number':123213,
    'e-mail':'zahid@gmail.com'      
       
               },
    
    "User2":{
    
    'roles':["admin","User"],
    'age':19,
    'name':'ahmet',
    'phone number':223233,
    'e-mail':'ahmet@gmail.com'      
       
            }
       
}
#users dictionarysinden user1 i yazdırdık
print(users['User1'])

#2.kullanıcının ismini yazdırdık
print(users['User2']["name"])

#user2 nin rollerini ekrana yazdırdık,bir uygualam yaparken admin olduğunu belirtmek için kullanabilriiz
#devamında birde [0] yazsaydım ekrana çıktı=admin olur
print(users['User2']["roles"])

#aynı değişkene farklı şeyler atadığımızda en son atadığımızı alır
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

#string int bool list bir arada kullanılabilir
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

#dict() methodu ile dictionari tanımlama
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

#kısaca list,tuple,set,dict arası farklar

# Liste (List),         sıralı ve değiştirilebilir bir koleksiyondur. Aynı öğelerden birden fazla bulunmasına izin verir.
# Demet (Tuple),        sıralı ve değiştirilemez bir koleksiyondur. Aynı öğelerden birden fazla bulunmasına izin verir.
# Küme (Set),           sırasız, değiştirilemez* ve indekslenemez bir koleksiyondur. Aynı öğelerden birden fazla bulunmaz.
# Sözlük (Dictionary),      sıralı** ve değiştirilebilir bir koleksiyondur. Aynı öğelerden birden fazla bulunmaz.
































