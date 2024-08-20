#liste tanımlama 
list1=["one","two","there"]
list2=["four","five","six"]

#list1 ile list2 yi topladık
numbers=list1+list2
print(numbers)
print(len(numbers))
print(numbers[2])


user1=["Çınar",23]
user2=["Ali",18]

#eğer böyle birleştirirsek listi(+ ile de oluyor ama lsit olduğu belli olmuyor)liste olduğu belli olur çıktıda parantezleri de alır
users=[user1,user2]
print(users)
#usersta 1. indeksi al, 1.userstaki 1.indeksi yazdır([1][0] olsaydı ali'yi yazdırırdı)
print(users[1][1])