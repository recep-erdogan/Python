#kullanıcıdan adını ve soyadını ayrı ayrı alsın
#eğer isim ve soyad uzunluğu 3 ten kısa 15 den uzunsa hata mesajı alsın
#herhangi sıkıntı soyka termialde merhaba ad soyad yazsın

isim = input("isminiz nedir? ")
soyad= input("soyadınız nedir? ")

if len(isim) < 3 or len(isim) > 15:
    print("lütfen geçerli giriş yapınız: ")
elif len(soyad) < 3 or len(soyad) > 15:
    print("lütfen geçerli giriş yapınız: ")
else:
    print(f"merhaba {isim} {soyad}")
