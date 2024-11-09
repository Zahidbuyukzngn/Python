# import sqlite3
# #engin hoca direkt veritabanı adını yazdı ama bende hata verdi.Bu yüzden yolu yazdım 
# connection=sqlite3.connect("C:/Users/Zahid/OneDrive/Masaüstü/YAZILIM/Python/enginDemiroğUdemy/chinook.db")

# #veriTabanı customers'dan isim soyisim aldık where city= diyerek sadece belirrtiğimiz şehirde olan kişileri yazdırdık
# #şehre tek tırnak koymazsan hata verir string anlar
# cursor=connection.execute("select FirstName,LastName from customers where city='Stuttgart'")

# for row in cursor:
#     print("First Name: " + row[0])
#     print("Last Name: " + row[1])
#     print("-----------------------------")


# # * ile tümünü aldık customers'ın.Şehri sadece stuttgart olan kişileri yazdırdım
# cursor2=connection.execute("select * from customers where city='Stuttgart'")

# for row in cursor2:
#     print("First Name: " + row[1])
#     print("Last Name: " + row[2])
#     print("Address: "+row[4])
#     print("-----------------------------")

# import sqlite3

# connection=sqlite3.connect("C:/Users/Zahid/OneDrive/Masaüstü/YAZILIM/Python/enginDemiroğUdemy/chinook.db")

# #or ile başka bir şehiri koşul gösterebiliriz
# #order by firstname ile sırlamayı adları alfabetik olarak sıralarız
# #desc ise tam tersini yapar.tersten sıralar.Burda eğer isimleri aynı olan 2 kişi olsaydı 
# #alfabetik olarak soyadındaki ilk harf en uzak olannı ilk yazdıracaktı
# cursor=connection.execute("select FirstName,LastName from customers order by FirstName,LastName desc")

# for row in cursor:
#     print("First Name: " + row[0])
#     print("Last Name: " + row[1])
#     print("-----------------------------")


#group by ve having

import sqlite3


connection=sqlite3.connect("C:/Users/Zahid/OneDrive/Masaüstü/YAZILIM/Python/enginDemiroğUdemy/chinook.db")

#şehre göre gurupladı(order by her zaman sona yazılır)
#having count(*)>1 ile ortak şehir sayısı sadece birden daha fazla olanları yazdırdı
cursor=connection.execute("select city,count(*) from customers group by city having count(*)>1")

#str çevirmezsek hata alırız.sayısal bir değer çıktığı için
for row in cursor:
    print("City: " + row[0])
    print("Count: " + str(row[1]))
    print("-----------------------------")