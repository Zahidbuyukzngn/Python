
while True:
    sayı=int(input("lütfen sayıyı girin: "))

    for i in range(2,sayı):
        if sayı % i == 0:
            print(f"{sayı} bir asal sayı değil. Tam böleni: {i}")
            break
        else:
            print(f"{sayı} bir asal sayıdır.")
            break
    devam=input("Tekrardan bir sayı girmek istiyor musunuz? (E/H): ").lower()