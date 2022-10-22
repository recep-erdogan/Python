index = 1
while index <= 5:
    print('*' * index)
    index = index+1
print("done")

guessCount = 1
while guessCount <= 5: #while dan sonraki koşul sağlandığı müddetçe döngünün içinde işlemi tekrar tekrar yapar
    guessCount += 1 #index 5ten küçü veya eşit olduğunda koşul sağlanmış olur
    print("index")
print("done") # while döngüsündeki şlem tamamen bitmeden sonraki komutlar işlemez

#kullanıcının 1 den 5'e bir tahmin yapmasını istediğimiz bir program yazalım kullanıcının üç tane tahmin etme hakkı olsun
#rasgele sayılar üretebilmek için random kütüphanesini ekleyelim

import random
randomNumber = random.randint(1,5) # bu komut 1 ve 5 arası 1-5 dahil rastgele tam sayı üretiyor
"""bir değişkenin ilerde kendimiz okurken veya başka birisi okurken daha anlaşılır olması için değişkeninisminin
ne işe yaradığını belli edecek türden isimlenidirmek önemlidir
yazdığımız bir değişkenin ismini değiştiriken ya program içindeki heryerde tek tek aadını değiştirmemiz lazım yada
değişkenin üstüne sağ tıklayıp refactor-->rename diyerek değiştirmemiz gerek"""
guessCount=0
guessLimit = 3
while guessCount <= guessLimit:
    guess = int(input("Enter your guess: "))
    guessCount += 1
    if guess == randomNumber:
        print("wou won!")
        break # break işletildiğinde koşul ne olursa olsun döngünün dışına çıkılır
else: #************ while'ın else'i **********
    """burda else ifle değil ehile ile aynı hizada! while'ın içindeki if bloğu çalışırsa break işletilir ve döngü kırılır
    ama eğer if komutu çalışmazsa else while'ın tekrarları tamamlanınca çalışır"""
    print("sorryi you failed!")