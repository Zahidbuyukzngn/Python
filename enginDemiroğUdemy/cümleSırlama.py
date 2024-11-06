cümle=str(input("Cümlenizi giriniz: "))

#split fonks eğer atamazsak çalışmaz 
bol=cümle.split()
#böl değişkenimizin üstüne sort ile sırlama yaptık baş harfe göre
bol.sort()

print(bol)
