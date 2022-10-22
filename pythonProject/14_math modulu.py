import math #math modülünü ekledik
print("1)",math.ceil(2.9))
#ceil metodu ondalıklı sayımıza en yakın büyük tam sayıyı döndürür
print("2)",math.ceil(-2.9))

print("3)",math.floor(2.9))
print("4)",math.floor(-2.9))
print("5)",-2.9//1) # floor taban bölmeyle aynı işi yapıyor fakat sonucunda float bir sonuç veriyor
print("6)",2.9//1)#taban bölmede işleme giren sayı flatsa sonuç float, floot da ne verirsek verelim sonucu int verir

print("7)",math.factorial(5)) #faktroriyel hesabı
print("8)",math.pi) # pi sayısı bizim tanımlayacağımızdan çok daha hassas bir şekilde kütüphanede mevcut
print("9)",math.tau) # tau ise pi sayısının 2 katını verir

print("10)",3 ** 2)
print("11)",3.0 ** 2) # sayı float olunca float int olunca int sonuç verir
print("12)",math.pow(3,2)) # pow komutu iki parametre alıyor ve sonucu her zaman float oluyor

