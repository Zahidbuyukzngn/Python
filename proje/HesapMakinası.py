

    
while True:
    
    sayıyıAl1=int(input("lütfen işlem yapmak istediğiniz 1. sayıyı giriniz: "))
    sayıyıAl2=int(input("lütfen işlem yapmak istediğiniz 2. sayıyı giriniz: "))

    hangiislem=input("yapmak istediğiniz işlemin işaretini yazınız(+,-,*,/): ")
    
    if hangiislem=="+":
     print("sayıların toplamı: ",(sayıyıAl1)+(sayıyıAl2))
   

    elif hangiislem=="-":
     print("sayıların çıkarımı: ",(sayıyıAl1)-(sayıyıAl2))

    elif hangiislem=="*":
     print("sayıların çarpımı: ",(sayıyıAl1)*(sayıyıAl2))

    elif hangiislem=="/":
       if sayıyıAl2 !=0:   
        print("sayıların bölümü: ",(sayıyıAl1)/(sayıyıAl2))
       else:
         print("Sıfıra bölme hatası!")

    else:
     print("Yanlış işlem girdiniz. Lütfen +,-,*,/ işaretlerinden birini giriniz.")

    devamMı=input("Bir işlem daha yapmak istiyor musunuz(E/H)").lower()

    if devamMı!="e":
     print("Tekrar görüşmek üzere!") 
     break
