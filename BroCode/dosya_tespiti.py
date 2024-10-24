import os 
#one drive da hata veriyor
#path değişkenine dosya yolunu ata.\\ koymayı unutma tek\ olmaz
path="C:\\pythondeneme.txt"

#eğer belge mevcutsa print yazdır
if os.path.exists(path):
    print("belge mevcut.")
    #isfile ile dosya olup olmadığını sorduk
    if os.path.isfile(path):
        print("bu bir dosya.")
        #isdir ile klasör mü diye sormuş olduk
    elif os.path.isdir(path):
        print("bu bir klasör")

#bulunamadıysa dosya bulunamadı yaz
else:
    print("dosya bulunamadı")
