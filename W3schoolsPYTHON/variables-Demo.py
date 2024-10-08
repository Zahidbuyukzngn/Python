'''
çoklu yorum satırına almak için bunu kullanabilirim

customer(müsteri) adi
soyadi
ad+soyad
cinsiyet 
kimlik no
doğum yili
yasadigi yer
yasi

'''
customerName="Mehmet Zahid"
customerLastName="Büyükzengin"
customerFullName=customerName+" "+customerLastName

customerGender=True #bool değişkeniyle ayarladık true erkek bayan false farzediyoruz 2 tane cinsiyet olduğu için

customerIDnumber="12345678910"

customerbirthYear =2005

whereTheCustomerLives="Konya,meram"

customerAge=2024-customerbirthYear

print(customerAge)
print(customerFullName)


'''
sipariş ücretleri toplama uygulaması
Order1 =142.5
Order2 =230
Order3 =553.99
'''
order1=142.5
order2=230
order3=553.99

total=order1+order2+order3
# , e dikkat et + yaptım hata aldım (;)
print("Total ",total)