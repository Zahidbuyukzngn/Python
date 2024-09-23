# kullanıcıYılı=int(input("lütfen hangi yılda doğduğunuzu giriniz: "))

# sıçanYıllari=[1924,1936,1948,1960,1972,1984,1996,2008]
# sıgıryıllari=[1925, 1937, 1949, 1961, 1973, 1985, 1997, 2009, 2021]
# parsyıllari=[1926, 1938, 1950, 1962, 1974, 1986, 1998, 2010, 2022]
# tavsanyıllari=[1927, 1939, 1951, 1963, 1975, 1987, 1999, 2011, 2023]
# balikyılları=[1928, 1940, 1952, 1964, 1976, 1988, 2000, 2012, 2024]
# yilanyılları=[1929, 1941, 1953, 1965, 1977, 1989, 2001, 2013, 2025]
# tavukyılları=[1933, 1945, 1957, 1969, 1981, 1993, 2005, 2017, 2029]


# if kullanıcıYılı in sıçanYıllari:
#  print("12 hayvanlı türk takvimine göre SIÇAN yılında doğmuşsunuz")

# elif kullanıcıYılı in sıgıryıllari:
#   print("12 hayvanlı türk takvimine göre SIĞIR yılında doğmuşsunuz")

# elif kullanıcıYılı in parsyıllari:
#   print("12 hayvanlı türk takvimine göre PARS yılında doğmuşsunuz")

# elif kullanıcıYılı in tavsanyıllari:
#   print("12 hayvanlı türk takvimine göre TAVŞAN yılında doğmuşsunuz")

# elif kullanıcıYılı in balikyılları:
#   print("12 hayvanlı türk takvimine göre BALIK-LU yılında doğmuşsunuz")

# elif kullanıcıYılı in yilanyılları:
#   print("12 hayvanlı türk takvimine göre YILAN yılında doğmuşsunuz")

# elif kullanıcıYılı in tavukyılları:
#   print("12 hayvanlı türk takvimine göre TAVUK yılında doğmuşsunuz")

# else:
#  print("12 hayvanlı türk takviminde girdiğiniz yıl tanımlı değildir")



 #daha kısa kod ile aynı işlemin yapımı


kullanicidanİNPUT=int(input("lütfen doğduğunuz yılı giriniz: "))

hayvanyılları={
    "sıçan":[1924,1936,1948,1960,1972,1984,1996,2008],
    "sığır":[1925, 1937, 1949, 1961, 1973, 1985, 1997, 2009, 2021],
     "pars":[1926, 1938, 1950, 1962, 1974, 1986, 1998, 2010, 2022],
   "tavşan":[1927, 1939, 1951, 1963, 1975, 1987, 1999, 2011, 2023],
    "balik":[1928, 1940, 1952, 1964, 1976, 1988, 2000, 2012, 2024],
    "yılan":[1929, 1941, 1953, 1965, 1977, 1989, 2001, 2013, 2025],
    "tavuk":[1933, 1945, 1957, 1969, 1981, 1993, 2005, 2017, 2029]
}


for hayvan,yıllar in hayvanyılları.items():
    if kullanicidanİNPUT in yıllar:
        print(f"12 hayvanlı türk takvimine göre {hayvan} yılında doğmuşsunuz")
        break  

else:
    print(f"girdiğiniz yıl olan {kullanicidanİNPUT} tanımlanmamıştır")    