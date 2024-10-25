import shutil
"COPY FİLE"
# source_path = Kopyalanacak dosya
# destination_path = Yeni dosyanın kopyalanacağı yer

source_path = "Dosyanın yolu \\ ile"
destination_path = "Dosyanın yolu\\ ile"

#Sadece dosyanın içeriğini kopyalar, 
#ancak dosya izinleri gibi diğer meta verileri kopyalamaz.
shutil.copyfile(source_path, destination_path)
print("Dosya başarıyla kopyalandı.")




import shutil

source_path = "C:\\Users\\Zahid\\OneDrive\\Masaüstü\\ornek.txt"
destination_path = "C:\\Users\\Zahid\\OneDrive\\Masaüstü\\kopya_ornek.txt"

# Dosyanın içeriğini ve dosya izinlerini kopyalar,
# ama diğer metadata (örneğin, son erişim tarihi) kopyalanmaz.
shutil.copy(source_path, destination_path)
print("Dosya başarıyla kopyalandı (içerik + izinler).")
#copyfile() ile benzer şekilde çalışır, ancak dosya izinlerini de kopyalar 
#(örneğin, okunabilirlik/yazılabilirlik gibi izinler).



import shutil

source_path = "C:\\Users\\Zahid\\OneDrive\\Masaüstü\\ornek.txt"
destination_path = "C:\\Users\\Zahid\\OneDrive\\Masaüstü\\kopya_ornek.txt"

# Dosyanın içeriğini, dosya izinlerini ve tüm metadata bilgilerini
#(örneğin, oluşturulma ve son erişim tarihleri gibi) kopyalar. Bu, tam bir kopyalama yapar.
shutil.copy2(source_path, destination_path)
print("Dosya başarıyla kopyalandı (içerik + izinler + metadata).")

#Bu fonksiyon, tüm dosya bilgilerini ve metadata (oluşturma tarihi, son erişim tarihi vb.) bilgilerini de kopyalar.
#Bu nedenle, en kapsamlı kopyalama fonksiyonudur.


"özet olarak"
# copyfile(): Sadece dosyanın içeriğini kopyalar.

# copy(): Dosyanın içeriğini ve dosya izinlerini kopyalar.

# copy2(): Dosyanın içeriğini, dosya izinlerini ve metadata bilgilerini kopyalar.