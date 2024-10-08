a,b,c,d=5,5,10,4

pasword="1234"
username="zahid1234"

Result=(a==b) #true
Result=(a==c) #false
Result=('zahid1234'==username) #true zahid1234 tanımladığımız username ye eşit
Result=('0000'==pasword) #false 0000 eşit değildir 1234'e
Result=(a!=b) # false çünkü  a ve b birbirine eşit
Result=(a!=c) # true çünkü  a ve c eşit değildir
Result=(a>=1) # doğru a 1 den büyük veya eşittir
Result=(a>b) # false a büyük değildir 5 den >= yapsaydık çıktı true olrudu

Result=(False==True) # 0 eşit değildir 1 e(false=0,true=1 demektir)
Result=(False+True+40) # false truelerle bir toplama işlemi



print(Result)


