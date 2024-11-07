import json

#users.json dosyasının projenin olduğu dosyada olmasıan dikkat et 
with open("users.json") as users:
    data = json.load(users)

#istediğimiz veriye [] ile ulaşabiliriz
print(data[0]["user_id"])
print(data[1]["nickname"])
print(data[4]["email"])

#bu şekilde içiçe olan jsonları da ayıklayabiliriz
print(data[0]["adress"]["city"])