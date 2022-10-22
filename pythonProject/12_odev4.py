"""program kullanıcadan bir string alsın bu stringi kullanarak yeni bir string oluştursunbu stringin
ilk 3 karakteriyle son 3 karakterinden oluşsun ancak tüm karakterler büyük harfli olacak şekilde sonuç versin
girdi 3 karakterden düşükse elde bulunan karakterlerle tamamlasın örn
ertuğrul girdisi RULERT at girdisi ATAT çıktısını versin"""

girdi = input("string bir ifade girin: ")
girdi = girdi.upper()
print(girdi[-3:] + girdi[0:3])

# girdi değeri at olduğunda 3. karakter eksik olsada kod çalışır 2 karakteri alır. eğer boşluk girersek yine çalışır
#hata vermez
