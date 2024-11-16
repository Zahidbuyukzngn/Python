"ABSTRACT CLASS- SOYUT SINIFLAR"
from abc import ABC,abstractmethod

#ABC yazmayı unutma
class futbol(ABC):
    #bu şekilde fonksiyonun abstract olduğunu bildiriyoruz
    @abstractmethod
    def sut(self):
        print("Şut atıldı")

    @abstractmethod
    def pas(self):
        print("Pas verildi")

#yukardaki sınıf abstract olsa da bu şekilde kullanabilirirz
#futbol clasındaki 2 fonksiyonu da tanımlamamız geriyor yoksa hata veriyor
#yukardan mesela pası fonk kaldırırsak aşağıda tanımlamamıza gerek kalmaz
class takım(futbol):
    def sut(self):
        print("Takım şut attı")
    
    def pas(self):
        print("Takım pas attı")

# #class abstract olduğu için sut fonksiyonu çalıştırılamadı
# fut=futbol()
# fut.sut()

takım1=takım()
takım1.sut()

