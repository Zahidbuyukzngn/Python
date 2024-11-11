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


# #group by ve having

# import sqlite3


# connection=sqlite3.connect("C:/Users/Zahid/OneDrive/Masaüstü/YAZILIM/Python/enginDemiroğUdemy/chinook.db")

# #şehre göre gurupladı(order by her zaman sona yazılır)
# #having count(*)>1 ile ortak şehir sayısı sadece birden daha fazla olanları yazdırdı
# cursor=connection.execute("select city,count(*) from customers group by city having count(*)>1")

# #str çevirmezsek hata alırız.sayısal bir değer çıktığı için
# for row in cursor:
#     print("City: " + row[0])
#     print("Count: " + str(row[1]))
#     print("-----------------------------")

#SELECT TE LİKE KOMUTU

# import sqlite3
# connection=sqlite3.connect("C:/Users/Zahid/OneDrive/Masaüstü/YAZILIM/Python/enginDemiroğUdemy/chinook.db")

# #where FirstName like '%s%' ==İÇİNDE S HARFİ OLAN İSİMLER
# #where FirstName like '%s' ==SONU S HARFİ İLE BİTEN İSİMLER
# #where FirstName like '%sa%' ==İSİMİN İÇİNDE SA OLAN İSİMLER
# #where FirstName like 's%' == S HARFİ İLE BAŞLAYAN İSİMLER

# cursor=connection.execute("select FirstName,LastName from customers where FirstName like 's%'")

# for row in cursor:
#     print("First Name: " + row[0])
#     print("Last Name: " + row[1])
#     print("-----------------------------")

#İNSTERT
def insertCustomer():
    import sqlite3
    connection=sqlite3.connect("C:/Users/Zahid/OneDrive/Masaüstü/YAZILIM/Python/enginDemiroğUdemy/chinook.db")
    #select deki gibi bir değere atamamıza gerek yok execute'yi
    #ilk önce değerleri verdik hangi değerlerden ekleme yapacağımızı,sonra  values( )le vereceğimiz değerleri belirttik
    #ayrıca veritabanı email belirtmeyi zorunlu kıldığı için mecbur email belirttik 
    connection.execute("""insert into customers 
                       (FirstName,LastName,city,email) 
                       values('Engin','Demiroğ','Ankara',
                       'engindemirog@gmail.com')""")
    #commit() ve close() yapmazsak değişiklikler gitmiyor.
    #commit() değişiklikleri kaydetmemizi sağlar, close() ise bağlantıyı kapatır.
    connection.commit()
    connection.close()

#insertCustomer()
#teriminalden cd ile proje dosyasını açmayı unutma yoksa çalışmıyor

"UPDATE"
def updateCustomer():
    import sqlite3
    connection=sqlite3.connect("C:/Users/Zahid/OneDrive/Masaüstü/YAZILIM/Python/enginDemiroğUdemy/chinook.db")
    
    #Ankara şehirlerini İstanbul ile değiştirdik.where city ile sadece ankara olanları değiştirdik
    connection.execute("""update customers set city='İstanbul'
                       where city='Ankara'""") 
    
    connection.commit()
    connection.close()

updateCustomer()