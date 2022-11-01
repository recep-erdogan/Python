print("1)",15+7)
print("2)",15-7)
print("3)",15*7)
print("4)",15/7)

print("5)",15//7) #bölme işemi yapar ondalıklı kısmı direkt siler
print("6)",15.7//1) #bölünen sayı float olduğu için sayıda float olur onlaıklı kısmı 0 olur
print("7)",15%7) # 15 mod 7
print("8)",15**7) # 15 üssü 7
x = 15**(1/3)
print("9)",x) # 15'in 3.dereceden kökünü aldık
print("10)",x ** 3) # 15 cevabı vermesi gerekirken 14.9 küsürlü bir sayı geldi yuvarlayabiliriz
x **=3
print("11)",round(x)) # round yuvarlama fonksiyonu

#mutlak değer için abs kullanılır
x = -3.9
print("12)",abs(x))

