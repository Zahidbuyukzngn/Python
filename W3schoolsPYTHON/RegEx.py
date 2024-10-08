#regex i import ettik
import re

#txt cümlesi the ile başlayıp spain ile mi bitiyor diye sorduk:

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

#eğer x ise evet 
if x:
  print("YES! We have a match!")
else:
  print("No match")


#Fonksiyon	Açıklama
'''
findall	    Tüm eşleşmeleri içeren bir liste döndürür
search	    Dizgede herhangi bir yerde bir eşleşme varsa, bir Match (Eşleşme) nesnesi döndürür
split	    Dizgenin her eşleşme noktasında bölündüğü bir liste döndürür
sub	        Bir veya birden fazla eşleşmeyi bir dizge ile değiştirir

'''

#[a-m] ile a ile m arasındaki harfleri txt stringinden aldık
import re

txt = "The rain in Spain"

#Find all lower case characters alphabetically between "a" and "m":

x = re.findall("[a-m]", txt)
print(x)


'''

[]	        Karakter kümesi	                                                            [a-m]
\	        Özel bir diziyi işaret eder (özel karakterlerden kaçış için kullanılır)	    \d
.	        Herhangi bir karakter (yeni satır karakteri hariç)	                    he..o
^	        Belirtilen karakterle başlar	                            ^hello
$	        Belirtilen karakterle biter	                                planet$
*	        Sıfır veya daha fazla tekrar	                            he.*o
+	        Bir veya daha fazla tekrar	                                 he.+o
?	        Sıfır veya bir tekrar	                                        he.?o
{}	        Tam olarak belirtilen sayıda tekrar	he.                         {2}o
|	 	    Ya, ya da                                   falls|stays
()	        Grubu yakala ve grupla	                                (abc)

'''


import re

txt = "hello planet"

#he ile başlayıp içinde o olan kelimeyi buldurduk
x = re.findall("he.*o", txt)
#p ile başlayıp n ye kadar yazdırdık
x=re.findall("p.+n",txt)


#planet ile mi bitiyor kelime diye sorduk
x = re.findall("planet$", txt)
if x:
  print("yes end with planet")
else:
    print("no")

print(x)

# ^ ile hello ile mi başlıyor diye sorduk
import re
txt2="hello planet"
x = re.findall("^hello", txt2)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")

"""

\A	    Belirtilen karakterler dizenin başında olduğunda eşleşme döndürür	    \AThe
\b	    Belirtilen karakterlerin kelimenin başında veya sonunda olduğu yerde eşleşme döndürür	    r"\bain"    r"ain\b"        
\B	    Belirtilen karakterler kelimenin başında veya sonunda olmadığında eşleşme döndürür	    r"\Bain"       r"ain\B"
\d	    Dize rakam (0-9 arası sayılar) içeriyorsa eşleşme döndürür	    \d
\D	    Dize rakam içermiyorsa eşleşme döndürür	    \D
\s	    Dize bir boşluk karakteri içeriyorsa eşleşme döndürür	\s
\S	    Dize boşluk karakteri içermiyorsa eşleşme döndürür	    \S
\w	    Dize herhangi bir kelime karakteri (a'dan Z'ye, 0-9 arası rakamlar, alt çizgi _ karakteri) içeriyorsa eşleşme döndürür	\w
\W	    Dize herhangi bir kelime karakteri içermiyorsa eşleşme döndürür 	\W
\Z	    Belirtilen karakterler dizenin sonunda olduğunda eşleşme döndürür	Spain\Z

"""

import re

txt = "The rain in Spain 42"

#sayıları almadan tüm harfleri tek tek yazar:

x = re.findall("\D", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
"""
[arn]	Belirtilen karakterlerden (a, r veya n) biri bulunduğunda eşleşme döndürür	[arn]
[a-n]	a ile n arasında alfabetik olarak bulunan küçük harflerle eşleşme döndürür	[a-n]
[^arn]	a, r ve n hariç herhangi bir karakterle eşleşme döndürür	    [^arn]
[0123]	0, 1, 2 veya 3 rakamlarından herhangi biri bulunduğunda eşleşme döndürür	[0123]
[0-9]	0 ile 9 arasında herhangi bir rakamla eşleşme döndürür	        [0-9]
[0-5][0-9]	00 ile 59 arasındaki iki basamaklı herhangi bir sayıyla eşleşme döndürür	[0-5][0-9]
[a-zA-Z]	a ile z arasında, küçük veya büyük harflerle eşleşme döndürür	    [a-zA-Z]
[+]	Kümelerde +, *, .,	, (), $, {} gibi semboller özel anlam taşımaz, bu nedenle [+] dizideki herhangi bir + karakteriyle eşleşme döndürür

"""

import re

txt = "8 times before 11:45 AM"

#a-z ve A-Z arasındaki tüm harfleri tek tek yazdırdı,sayıları almaz:

x = re.findall("[a-zA-Z]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


#^arn ile arn harfleri hariç diğer harfleri yazdırıdk
import re

txt = "The rain in Spain"

#Check if the string has other characters than a, r, or n:

x = re.findall("[^arn]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")



import re

#"ai" geçen kelimeler var mı diye sorduk:

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)


import re

#\s ile kelime kelime böler split
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

#\s ile böldürdük ama 1 yazarak sadece 1 kere böldürdük
import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

#sub bölerken aralarına 9 koyar
import re

txt = "The rain in Spain"
x = re.sub("\s", " 9 ", txt)
print(x)


import re

#sub ile 2 kere olduğunu belirttik

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)


#search ile he kaçıncı indekste başlar ve biter onu yazdırdık
import re

txt = "The rain in Spain"
x = re.search("he", txt)
print(x)


"""
.span() eşleşmenin başlangıç ve bitiş konumlarını içeren bir tanımlama grubu döndürür.
.string, işleve geçirilen dizeyi döndürür
.group() dizenin eşleşme olan kısmını döndürür
"""

import re

#Search for an upper case "S" character in the beginning of a word, and print its position:

txt = "The rain in Spain"
#\w+: Bir veya daha fazla kelime karakteri (harfler, rakamlar ve alt çizgi) ile eşleşir. Bu, 'S' ile başlayan kelimenin geri kalanını bulur.

x = re.search(r"\bS\w+", txt)
# Eşleşmenin başlangıç ve bitiş pozisyonlarını bulalım
print(x.span())


#Bu kod, "The rain in Spain" metninde büyük harf 'S' ile başlayan bir kelimeyi aramakta ve ardından bu kelimenin bulunduğu orijinal diziyi ekrana yazdırmaktadır.
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)



#Bu kod, "The rain in Spain" metninde büyük harf 'S' ile başlayan bir kelimeyi arar ve bu kelimeyi ekrana yazdırır. Aşağıda kodu adım adım açıklıyorum:
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
