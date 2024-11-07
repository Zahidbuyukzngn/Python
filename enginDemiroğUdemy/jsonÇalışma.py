import json

# JSON formatında bir metni Python sözlüğüne dönüştürmek için loads kullanılır
users = '{"isim":"mehmet","soyisim":"paşa"}'
usersJson = json.loads(users)  # JSON metnini Python sözlüğüne çevirir
print(usersJson["isim"])

# Python sözlüğünü JSON formatında bir metne dönüştürmek için dumps kullanılır
users2 = {
    "yas": 29,
    "sehir": "konya"
}
users2Json = json.dumps(users2)  # Python sözlüğünü JSON metnine çevirir
print(users2Json)



