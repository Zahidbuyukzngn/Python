# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# #hem color keyini ekledik hem de red valuesini eklemiş oldum
# thisdict["color"] = "red"
# print(thisdict)


#eklmeyi bu şekilde de yapabiliriz
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
print(thisdict)

user1={
    "adi":"ahmet",
    "soyad":"ak",
    "numara":"1"
}

user2={
    "adi":"hasan",
    "soyad":"yel",
    "numara":"2"
}
user1.update({"Sehir":"Konya"})
user2.update({"Sehir":"Ankara"})

result=f"{user1} another {user2}"
print(result)