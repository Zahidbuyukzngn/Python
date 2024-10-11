#i 6 ya eşşit veeya büyük olursa print durur

# i = 1
# while i < 6:
#   print(i)
#   i=i+1
#   #veya i+=1


# #i 3 e eşit olana kadr artar 3 de finish.
# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1

# #burda while de 12 verdik ama içinde if bloğu olduğu için o bloktada 8 koşul olduğudan
# #12 ye gelmeden 8 de yazdırma biter
# i=1
# while i<12:
#   print(i)
#   if i==8:
#     break
#   i+=1
  
# #CONTİNUE
# #continue ile devam ettirebililyoruz
# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)
   

# #while içinde ELSE kullanımı
# #Koşul yanlış olduğunda bir mesaj yazdırır
# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")


'0\'dan 100e kadar sayıların toplamı' 

x=0
toplam=0
while x<=100:
  toplam+= x
  x+=1
  print(toplam)