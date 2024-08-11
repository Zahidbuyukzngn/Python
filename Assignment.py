# x,y,z=6,2,3

#ctrl+k yap sonra ctrl +c
#ctrl +C ile kısayola alma

# x +=5     x=x+5
# x -=1     x = x-1
# y *=2     y=y*2
# y /=1     
# x %=5
# y //=2    y=y//2
# x **=5    x=x**5

values=1,4,3,32,111

print(values)
print(type(values))

#normalde her virgül bir value sayılır ama burda a,*b dedik ve normalde hata vermesi gereken kod bir dizi halinde 
#kalan değerleri içine yazdırdı ve bu sayede kodumuz hata almadı
a,*b=values

print(a,b)
#burada ise b ye diğer sayıları tutması için bir dizi oluşturmuştuk ya o dizideki 1.indeksteki sayıyı getirmesini sağlıyoruz
print(a,b[1])