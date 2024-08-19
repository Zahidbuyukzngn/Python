name="Mehmet Zahid"
surname="Büyükzengin"
age=19

#selamlama
greeting=("My name is "+name+" "+surname+" and \nI am "+str(age)+" years old")    


#len ile kaç tane diziden oluşuyor onu yazdı c# daki gibi 0 dan başlıyor
lenght=len(greeting)
print(lenght)


print(greeting)
#greeting cümlesindeki 5. harfi yazdırdık
print(greeting[5])

#sondan başlar -1 de çıkdı d
print(greeting[-1])

#3.karakterden başla 8.karaktere kadar yazdır
print(greeting[3:8])

#0 dan 17ye kadar yazdır
print(greeting[ :17])

#5 den başla son kadar yazdır
print(greeting[5: ])

#0 dan başla her index aldıktan sonra 1 karakter atla 11 e kadar devam ettir
print(greeting[0:11:2])

#greattingi tersten yazdırma +satır ekleme
print("\n",greeting[::-1])

#string cümle içine tırnak içinde bir şey eklemek istersek \\ eklemek zorundayız
txt = "We are the so-called \"Vikings\" from the north."

'''
\'	Single Quote	tırnak işareti kullanma
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value
'''
