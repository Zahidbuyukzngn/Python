try: 
    with open("text.txt") as file:
        print(file.read())

#ismini verdiğimiz dosya bulunamzsa 
except FileNotFoundError:
    print("böyle bir dosya bulunamadı")

#DOSYANIN ÜZERİNE BİRŞEYLER YAZDIRMA
text="python with bro code:)"+" hi everyone"

with open("text.txt","a") as file:
    file.write(text)


#"w": Yazma modunda açar, dosya varsa içeriğini siler.dosya yoksa oluşturur
#"a": Ekleme modunda açar, dosya varsa sonuna ekleme yapar.dosya yoksa oluşturur
#"r": Sadece okuma modunda açar, dosya yoksa hata verir.