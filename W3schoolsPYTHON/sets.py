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