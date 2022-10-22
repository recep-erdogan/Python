#TC kimlik numarasını kontrol eden program
#doğrulamak için  1,3,5,7 ve.9 hanelerindeki rakamların toplamını 7ile çarpımından çıkan sonucu
#2,4,6 ve 8.hanelerin rakamlarının toplamından çıkarıldığında geriye kalanın 10'a böldüğümüzde kalanı 10. haneyi verir.
#1. haneden 10. haneye kadar olan tüm rakamların toplamını 10'a böldüğümüzde kalanı 11. rakamı verir.

#[(tekler(11 hariç) x 7) - (çiftler) ] / 10 = 10.basamak
#(1. - 10. bas hepsinin toplamı) % 10 = 11. basamak

tckimlikno = input("Tc kimlik numaranızı girin: ") #input("Tc kimkik no girin")


def islem1(sayi1: str) -> bool:
    tekler = 0
    ciftler = 0
    sonuc1 = 0
    # basamak sayısı doğruysa yapılacak işlemler
    for tekrakam in range(0, 10, 2):
        tekler += int(sayi1[tekrakam])
        # 1,3,5,7,9. basamak toplamları
        #print("tekler",tekler)
    for ciftrakam in range(1, 9, 2):
        ciftler += int(sayi1[ciftrakam])
        #print("ciftler",ciftler)
        # 2,4,6,8. basamak toplamları
    sonuc1 = (tekler * 7 - ciftler) % 10
    if int(sayi1[9]) == sonuc1:
        return True
    else:
        return False
islem1(tckimlikno)


def islem2(sayi2: str) -> bool:
    geneltoplam = 0
    for genel in range(0, 10, 1):
        geneltoplam += int(sayi2[genel])
        # 1.-10. basamkların toplamı
    geneltoplam %= 10
    if geneltoplam == int(sayi2[10]):
        return True
    else:
        return False

if len(tckimlikno) == 11:
    if islem1(tckimlikno) and islem2(tckimlikno):
        print("gecerli Tc kimlik no.")
    else:
        print("hatalı Tc kimlik no")

else:
    print("Basamak sayısını yanlış girdiniz")
