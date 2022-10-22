""" kullanıcının evi ve işyeri arasındaki uzaklığın metresi sorulsun ve terminale kilometre olarak dönüş alınsın"""
#kendi çözümüm
mesafe = int(input("ev-isyeri arasındaki mesafe kaç metre? "))
intDeger = (mesafe // 1000)
floatDeger = (mesafe % 1000)
print(str(mesafe//1000)+","+str(mesafe%1000))