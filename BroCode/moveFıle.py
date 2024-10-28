import os 

#dosya adını en sona yaz
source="C:\\Users\\Zahid\\OneDrive\\Masaüstü\\YAZILIM\\Python\\BroCode\\dosyadeğiştirme.txt"
destination="C:\\Users\\Zahid\\OneDrive\\Masaüstü\\dosyadeğiştirme.txt"

try:
   
   
    if os.path.exists(destination):
     print(" dosya zaten burada")
    
    #sola kaynak yani dosyanın yolu,bro code adını yazdı ama bende olmadı
    #sağa ise dosyanın gideceği yolu yazıyoruz
    else:
     os.replace(source,destination)
     print(source+" dosya taşındı")

except FileNotFoundError:
 print(source+" dosya bulunamadı")