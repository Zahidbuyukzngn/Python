#3 sözlük içeren bir dict
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# #veya 3 dict oluştur ve myfamily de bunları dict e çevir
# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }

# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }

#tobiası yazdırmış olduk
print(myfamily["child2"]["name"])


#İç içe geçmiş tüm sözlüklerin anahtarları ve değerleri arasında geçiş yapabiliriz
#ilk dögüde child1 i yazdırdık,altındaki for da ise child1 in içindeki değerleri
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])
