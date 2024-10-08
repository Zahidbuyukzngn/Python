#remove ile kaldırma işlemi
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")

print(thisset)

#aynsını discard ile de yapabiliriz
thisset = {"apple", "banana", "cherry"}
thisset.remove("apple")

print(thisset)

#rastgele bir elemanı pop ile silme
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()

print(x)
print(thisset)

#tüm kümeyi boşaltır
thisset = {"apple", "banana", "cherry"}
thisset.clear()

print(thisset)

#kümeyi tamamen silecektir
thisset = {"apple", "banana", "cherry"}
del thisset

print(thisset)

















