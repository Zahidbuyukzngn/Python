ısıklar=["red","yellow","green"]

hangiısık=ısıklar[2]
print(hangiısık)

if hangiısık == "red":
    print("DUR!")

elif hangiısık == "yellow":
    print("HAZIRLAN!")

elif hangiısık == "green":
    print("GEÇ!")
    #GECE 12'DEN SONRA LAMBALAR YANMADIĞI İÇİN ELSE ÇALIŞIR
else:
    print("DİKKATLİ GEÇ!")