# Create a function which multiply two numbers

numbers=[1,2,3,4,5,6,7,8,]
sorted_numbers=sorted(numbers)
print(numbers)



#CD .. ile bir geri dosyaya gelir
#\t ile 4 tane boşluk bırakabiliriz
print("bugün mecidiye'den kadıköy'\e 1 saatte geldim")  


# Bazen döngülerde bir şart sağlandığında bir sonraki iterasyondan devam etmek isteyebilirim. Bunu continue ile sağlayacağız.
# continue komutu ile karşılaşıldığı zaman, döngünün bir sonraki iterasyonuna geçilir.

#bu örnekte 3ü yazdırmadan direkt geçti
#eğer altında bir işlem varsa onu yapmayacak(forun içi için geçerli)(mesela 1yi ikişer ikişer arttırmak istesek arttıramayız)
for i in range(10): 
    if i == 3: continue
    print(i)
    
    
