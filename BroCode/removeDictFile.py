import os 
import shutil

#silinecek dosya klasör adı
path="deneme123"

try:
    #sadece dosya silmek için remove kullanılabilir
    os.remove(path)

    #rmdir ile içi boş klasörleri silebiliriz
    #os.rmdir(path)
    
    #kullanımı çok risklidir! içi dolu veya boş olan klasörü siler
    #shutil.rmtree(path)
    
    
except PermissionError:
    print(f"{path} dosyasına erişim izniniz yok")

except FileNotFoundError:
    print(f"{path} dosyası bulunamadı")

else:
    print(f"{path} dosyası silindi")