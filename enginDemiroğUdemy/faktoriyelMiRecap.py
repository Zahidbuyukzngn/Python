faktoriyel=int(input("Faktoriyeli alınmasını istediğiniz sayıyı giriniz: "))

if faktoriyel<0:
    print("Faktöriyel hesaplaması için negatif bir sayı giremezsiniz.")
elif faktoriyel ==0:
    print("Faktöriyel 1'dir.")
else:
    faktoriyel_hesap=1
    for i in range(1,faktoriyel+1):
        faktoriyel_hesap *= i
    print(f"{faktoriyel} sayısının faktöriyeli: {faktoriyel_hesap}")