# Setleri kümeler olarak düşünebiliriz.


# Sadece özgün değerleri tutan, içerisinde bir eleman var mı yok mu, başka bir setle hangi elemanları farklı gibi işlemleri performanslı bir şekilde yapabileceğimiz bir veri yapısıdır.


# Dictionary'ler gibi eleman sorgusu yapmak hızlıdır. Dictionarylerde key-value çift olarak bulunduğu için aynı uzunluktaki bir setten daha fazla yer kaplar.


# Setler indexlenemez.


# Setler mutable'dır.

#Setin içinde bir elemanı birden çok göremezsiniz.(1,2,3,4,1 setinde çıktı 1,2,3,4 olur)


# Difference (fark)
#fark alma: s1 kümesi ile s2 kümesinin farkı (s1 – s2) veya (s1 \ s2)

# s1 in hangi elemanları s2 den farklıdır.
#s1.difference(s2)


# Symmetric Difference
# s1'in s2 den farkı ile s2'nin s1 den farkının birleşimi. (s1 \ s2) U (s2 \ s1) - > s1 U s2 - (s1 n s2)

# U -> Birleşim
# n -> kesişim



# Subset (Alt küme)
# s1.issubset(s2), s1'in s2'nin alt kümesi olup olmadığını kontrol eder


# Superset (üst küme)
# s2.issuperset(s3) s2'nin s3'ün üst kümesi olup olmadığını sorgular







#Set öğelerinde ayarlanan öğeler değiştirilemez ancak öğeleri kaldırabilir 
#ve yeni öğeler ekleyebilirsiniz.

#Setler sırasızdır, dolayısıyla öğelerin hangi sırayla görüneceğinden emin olamazsınız.
#her seferinde farkl bir sıralama yapabilir

#set tanımlamak için kullanılabilir
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

fruits={"apple","Banana"}

for x in fruits:
    print(x)

fruits.add('cherry')
fruits.update(["mango","watermelon"])
    
    #kaldırma işlemi bu iki fonksiyonla da yapabiliriz
fruits.remove("mango")
fruits.discard("apple")

#liste başındaki eleman siliniyor [] li dizide ise sondakini siler
fruits.pop()

print(fruits)

mylist=[1,2,3,4,5,1,2,3]
print(mylist)
#set fonksiyonuyla dizide tekrarlayan sayıları sildi
print(set(mylist))

#burda bir set tanımlamış olduk
İsimler={"ali","veli","mustafa","ahmet"}

print(İsimler)

#0 ve 1'i  bu şekilde ekrana yazdıramayız.0 ve 1 true-false ye denktir
#eğer set de true false varsa 0 ve 1 çıktıda gözükmez
thisset = {"apple", "banana", "cherry",False,True, 0}

print(thisset)

#banana b setin içindemi diye sorduk result TRUE
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

#not in ile içinde değil demi diye sordurduk
#çıktı tabiki false çünkü banana setin içnde mevcut
thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)