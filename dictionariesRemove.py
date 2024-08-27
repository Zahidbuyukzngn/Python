#belirtilen keyi ve onunla birlikte anahtarı da siler

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)


#eklenen son öğeyi siler popitem()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "speed":260
}
thisdict.popitem()
print(thisdict)

#del de aynı işlevi görür ayrıca del thisdict yaparsak tüm dicti siler
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

#dictin içini boşaltır çıktı {}
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)