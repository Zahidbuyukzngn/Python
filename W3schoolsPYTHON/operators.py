# % ile mod alır kalanı çıktı verir.10u 3e bölüp kalanı yazdırır

# ** ile üs alır.5**2 (5 üzeri 2 demektir)

# // ile sayıları böler ama sonucu en yakın  basamağa yuvarlar değer float olmaz


"""
=	    x = 5	    x = 5	
+=	    x += 3	    x = x + 3	
-=	    x -= 3	    x = x - 3	
*=	    x *= 3	    x = x * 3	
/=	    x /= 3	    x = x / 3	
%=  	x %= 3	    x = x % 3	
//=	    x //= 3	    x = x // 3	
**=	    x **= 3 	x = x ** 3	
&=	    x &= 3	    x = x & 3	
|=	    x |= 3	    x = x | 3	
^=	    x ^= 3	    x = x ^ 3	
>>=	    x >>= 3	    x = x >> 3	
<<=	    x <<= 3	    x = x << 3	
:=	  print(x := 3)	    x = 3
print(x)


"""

"""
==    Eşit                x == y
!=    Eşit değil          x != y
>     Büyük               x > y
<     Küçük               x < y
>=    Büyük veya eşit     x >= y
<=    Küçük veya eşit     x <= y

"""


"""
and    Her iki ifade de doğruysa True döner               x < 5 and  x < 10
or     İfadelerden biri doğruysa True döner               x < 5 or x < 4
not    Sonucu tersine çevirir, sonuç doğruysa False döner    not(x < 5 and x < 10)

"""
#sayı 4 yapınca kod çalışmaz ama 15 yapınca çalışır not zıtlık yapıyor 
x=15
if not(x <5 and x<10):
    print("sayı 5 ve ondan küçük")

"""

is       Her iki değişken de aynı nesneyse True döner                 x is y
is not   Her iki değişken de aynı nesne değilse True döner            x is not y

"""    

"""
in        Belirtilen değere sahip bir dizi nesnenin içinde varsa True döner          x in y
not in    Belirtilen değere sahip bir dizi nesnenin içinde yoksa True döner          x not in y

"""

"""
&     VE            Her iki bit de 1 ise, her biti 1 yapar                              x & y
|     VEYA          İki bitten biri 1 ise, her biti 1 yapar                             x | y
^     ÖZEL VEYA     İki bitten yalnızca biri 1 ise, her biti 1 yapar                    x ^ y
~     DEĞİL         Tüm bitleri tersine çevirir                                         ~x
<<    Sola kaydırma  Sola kaydırma, sağdan sıfırları ekler ve en soldaki bitleri düşürür x << 2
>>    Sağa kaydırma  Sağa kaydırma, soldan en soldaki bitin kopyalarını ekler ve en sağdaki bitleri düşürür  x >> 2

"""