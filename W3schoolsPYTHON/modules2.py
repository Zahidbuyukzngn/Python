
#modules dosyasından modules2 ye bilgi alma işlemleri

#Bir modülü içeri aktarırken as anahtar sözcüğünü kullanarak bir diğer ad oluşturabilirsiniz:
import modules as mx

a = mx.person1["age"]
print(a)

import modules

a = modules.person1["age"]
print(a)
b= modules.person1["country"]
print(b)

#windows çıktısı aldık
import platform

x = platform.system()
print(x)

#Bir modüldeki tüm işlev adlarını (veya değişken adlarını) listelemek için yerleşik bir işlev var. => dir() fonksiyonu:
#Bu kod, platform modülünün içinde bulunan tüm fonksiyonları ve özellikleri ekrana yazdırır. 
#dir() sayesinde hangi fonksiyonların kullanılabilir olduğunu görebilir ve modülün işlevleri hakkında bilgi sahibi olabilirsin.

import platform

x = dir(platform)
print(x)


#sadece age ifadesini import etmek istiyorsak print ksımına köşeli parantez koyabilirim
#modules projesinden sadece person1'i çektik
from modules import person1

print(person1["age"])
