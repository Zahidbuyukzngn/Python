import sqlite3
#engin hoca direkt veritabanı adını yazdı ama bende hata verdi.Bu yüzden yolu yazdım 
connection=sqlite3.connect("C:/Users/Zahid/OneDrive/Masaüstü/YAZILIM/Python/enginDemiroğUdemy/chinook.db")

#veriTabanı customers'dan isim soyisim aldık where city= diyerek sadece belirrtiğimiz şehirde olan kişileri yazdırdık
#şehre tek tırnak koymazsan hata verir string anlar
cursor=connection.execute("select FirstName,LastName from customers where city='Stuttgart'")

for row in cursor:
    print("First Name: " + row[0])
    print("Last Name: " + row[1])
    print("-----------------------------")


# * ile tümünü aldık customers'ın.Şehri sadece stuttgart olan kişileri yazdırdım
cursor2=connection.execute("select * from customers where city='Stuttgart'")

for row in cursor2:
    print("First Name: " + row[1])
    print("Last Name: " + row[2])
    print("Address: "+row[4])
    print("-----------------------------")
