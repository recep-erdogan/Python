sampleString = "Python is general purpose programming language"
print("1)",len(sampleString))
#stringin kaaç karakerden öğrenmek istediğimizde (karakter uzunluğu) len fonksiyonu kullanır.(lengh)
#ileride listelerin kaç elemanı olduğunu da bulmakta kullanılacak

#bir stringte bütün harfleri büyülten veya küçülten vb birçok fonksiyon mevcut bunları sampleString.fonsiyonadı
#şeklinde baklıabilir noktayı yazdıktan sonra birsürü fonksiyon sıralanır bu fonksiyonlara metod denir.
sampleString.upper()
#print, input len gibi fonksiyonlar genel amaçlı olup nesnelere bağlı değildir, upper gibi metodları kullanmak içinse
#nesneye ihtiyaç vardır bu metodla fonksiyonun en büyük farkıdır
print("2)",sampleString.upper())
print("3)",sampleString) #uppper metodu sampleString değişkeninin normal değerini değiştirmiyor
#eğer sampleStringin normal değerini değiştirmek istersek şöyle yaparız
sampleString = sampleString.upper()

print("4)",sampleString)
print("5)",sampleString.lower())# aynı şekilde tüm harfleri küçük olarak yazdırıdık
print("6)",sampleString.title()) # kelimelerin ilk harfini büyük diğerlerini küçük harfe dönüştürdük

print("7)",sampleString.find("P")) # metnin içindeki ilk P bulunana elemanın indis numarası 0 olduğu için 0 çıktısı alınır
print("8)",sampleString.find("o")) # 4 sonucunu verir o nun bulunduğu ilk yer 4. index
#find metodunda küçük büyük duyarlılığı vardır, o yerine O aratırsak -1 değerini döner, aratılan şey yoksa sonuç -1 dir
print("9)",sampleString.find("O"))

sampleString = sampleString.title() #işlemi kalıcı olrak değiştridik tekrardan

print(sampleString.find("General Purpose")) # uzunca bir string de aratılabilir
#çıkan 10 sonucu aranan kelimenin 10. indisten itibaren başladığını belirtir

print("10)",sampleString.replace('general purpose','high level'))
#replace de find gibi çalışır ilk parametresi arayıp bulacağı ifade diğeri ise bulduğunda onun yerine yazacağı ifade
print("11)",sampleString.replace("P","J"))

print("12)","P" in sampleString) # sampleStringin içinde P varmı diye sorgulattık varsa True yoksa False döndürecek
#uzunca bir şey de aratılabilir
print("13)","Python" in sampleString)
print("14)","Jython" in sampleString)

print("15)",sampleString.count('P')) #stringimizin içinde kaç tane P var diye baktık ve yazdırdık
print("16)",sampleString.count('p'))
print("17)",sampleString.count('Python'))

sampleString = sampleString.lower()
print("18)",sampleString.find("p")) # find soldan bakıp bulduğu ilk indisi yazıyordu
print("19)",sampleString.rfind("p")) # rfind ise sağdan bakıp ilk indis numarasını verir