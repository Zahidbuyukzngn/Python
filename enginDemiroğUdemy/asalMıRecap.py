while True:
    sayı = int(input("Lütfen sayıyı girin: "))

    if sayı <= 1:
        print(f"{sayı} bir asal sayı değildir.")
    else:
        for i in range(2, sayı):
            if sayı % i == 0:
                print(f"{sayı} bir asal sayı değil. Tam böleni: {i}")
                break
        else:
            # for döngüsü break yapılmadan biterse sayı asaldır
            print(f"{sayı} bir asal sayıdır.")

    devam = input("Tekrardan bir sayı girmek istiyor musunuz? (E/H): ").lower()

    if devam != "e":
        print("Programdan çıkılıyor...")
        break