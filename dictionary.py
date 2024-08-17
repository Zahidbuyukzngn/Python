
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