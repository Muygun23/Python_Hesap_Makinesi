print("""**************************

HESAP MAKİNESİ PROGRAMI

Şimdilik Yapabildiğim İşlemler:

1. Toplama İşlemi
2. Çıkarma İşlemi
3. Çarpma İşlemi
4. Bölme İşlemi
5. Faktöriyel Bulma
6. Karakök Bulma
7. Mutlak Değer Alma
8. Bölümünden Kalma
9. Logaritma Hesaplama
0. Çıkış

**************************""")

import time
import math

while True:
    islem = int(input("Lütfen Yapmak İstediğiniz İşlem Numarasını Giriniz:"))
    if islem == 0:
        print("İşleminiz Sonlandırılıyor.")
        time.sleep(1)
        print("Tekrar Bekleriz...")
        break

    elif islem == 1:
        print("Toplama İşlemini Seçtiniz..")
        time.sleep(0.5)
        sayi1 = int(input("1. sayıyı giriniz:"))
        sayi2 = int(input("2. sayıyı giriniz:"))
        print("İşleminiz Gerçekleşiyor...")
        time.sleep(1)
        print("{} + {} = {}".format(sayi1,sayi2,sayi1+sayi2))

    elif islem == 2:
        print("Çıkarma İşlemini Seçtiniz..")
        time.sleep(0.5)
        sayi1 = int(input("1. sayıyı giriniz:"))
        sayi2 = int(input("2. sayıyı giriniz:"))
        print("İşleminiz Gerçekleşiyor...")
        time.sleep(1)
        print("{} - {} = {}".format(sayi1,sayi2,sayi1-sayi2))

    elif islem == 3:
        print("Çarpma İşlemini Seçtiniz..")
        time.sleep(0.5)
        sayi1 = int(input("1. sayıyı giriniz:"))
        sayi2 = int(input("2. sayıyı giriniz:"))
        print("İşleminiz Gerçekleşiyor...")
        time.sleep(1)
        print("{} x {} = {}".format(sayi1,sayi2,sayi1*sayi2))

    elif islem == 4:
        print("Bölme İşlemini Seçtiniz..")
        time.sleep(0.5)
        sayi1 = int(input("1. sayıyı giriniz:"))
        sayi2 = int(input("2. sayıyı giriniz:"))
        print("İşleminiz Gerçekleşiyor...")
        time.sleep(1)
        print("{} / {} = {}".format(sayi1,sayi2,sayi1/sayi2))

    elif islem == 5:
        print("Faktöriyel Bulma İşlemini Seçtiniz..")
        time.sleep(0.5)
        sayi1 = int(input("Faktöriyelini almak istediğiniz sayıyı giriniz:"))
        print("İşleminiz Gerçekleşiyor...")
        time.sleep(1)
        print("{} sayısının faktöriyeli = {}".format(sayi1,math.factorial(sayi1)))

    elif islem == 6:
        print("Karekök Bulma İşlemini Seçtiniz..")
        time.sleep(0.5)
        sayi1 = int(input("Karekökünü almak istediğiniz sayıyı giriniz:"))
        print("İşleminiz Gerçekleşiyor...")
        time.sleep(1)
        print("{} sayısının karakökü = {}".format(sayi1,math.sqrt(sayi1)))

    elif islem == 7:
        print("Mutlak Değer Alma İşlemini Seçtiniz..")
        time.sleep(0.5)
        sayi1 = int(input("Mutlak Değerini almak istediğiniz sayıyı giriniz:"))
        print("İşleminiz Gerçekleşiyor...")
        time.sleep(1)
        print("{} sayısının mutlak değeri = {}".format(sayi1,math.fabs(sayi1)))

    elif islem == 8:
        print("Bölümünden Kalma İşlemini Seçtiniz..")
        time.sleep(0.5)
        sayi1 = int(input("1. Sayıyı giriniz:"))
        sayi2 = int(input("2. Sayıyı giriniz:"))
        print("İşleminiz Gerçekleşiyor...")
        time.sleep(1)
        print("{} sayısının {} bölümünden kalan = {}".format(sayi1,sayi2,math.fmod(sayi1,sayi2)))

    elif islem == 9:
        print("Logaritma Hesaplama İşlemini Seçtiniz..")
        time.sleep(0.5)
        sayi1 = int(input("1. Sayıyı giriniz:"))
        sayi2 = int(input("2. Sayıyı giriniz:"))
        print("İşleminiz Gerçekleşiyor...")
        time.sleep(1)
        print("{} sayısının ve {} sayısının logaritması = {}".format(sayi1,sayi2,math.log(sayi1,sayi2)))


    else:
        print("Hatalı Tuşlama Yaptınız..")
        time.sleep(1)
        print("Lütfen Tekrar Deneyiniz:")
        continue