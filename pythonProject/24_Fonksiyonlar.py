def greetUser():
    print('Hi Ahmet')
    print('welcome my home')
#programın pekçok yerinde yapacağımz bir işlem varsa onu fonksiyon haline getirip tekrar aynı kodları yazmak zahmetinden
#kurtuluru. fonkisyonlar çağırılmadığı sürece çalışmazlar .
#bir fonksiyo bloğunu çağırmadan önce fonksiyonun tanımlanmış olması gerekiyor
#bir fonksiyonu tanımladıktan öncesinde v sonrasında iki satır boşluk bırakmazsak altı sarı çizik olarak uyarı verir
#bu uyarılar öneri olup peb8 diye bir dökümanda yayınlanıyorlar.

#fonksiyonlaraa parametre eklenebilir.
def greetUser2(firstName,lastName):
    print(f"Hi {firstName} {lastName}")
    print('welcome my home')

#argümanla paratmetre aynı şey değildir!!
#Argümanlar fnksiyonlara gönderilecek değerler olup fonksiyonların çağrılma anlarında set edililer
#parametreler fonksiyonlar tanımlanırken gelecek olan argüman değerini bir değişken gibi barındırmak için tanımlanırlar

greetUser2('recep',"erdogan") #pozitionly argüman atamsası. bu atamada sıraların doğru girilmesi lazım
#anahtar kelimesi belirttiğimiz argümanlarda tanımlama yaptığımız için karışıklığa mahal verilmemiş  oluyor
greetUser2(lastName='erdogan', firstName='recep') #keyword argüman

def greetUser3(firstName, lastName, message):
    print(f"Hi {firstName} {lastName}")
    print(message)

greetUser3('recep',message='welcome my home', lastName='erdogan')
# argümanların bazılarını keyword bazılarını pozitiyonly verbiliriz argümanların ilki pozitionl olması keywprdden sonra
#yazamayız

#fonksiyonda bir varsayıla deeğer tanımlaması yapabiliriz. eğer fonksiyonda bir parametre tanımlanmışsa ve bir
#argüman set edilmemişse varsayılan değer kullanılır.

def greetUser4(firstName, lastName, message = 'welcome my home')
    print(f"Hi {firstName} {lastName}")
    print(message)

greetUser4(firstName="recep", lastName="erdogan")

def getGreetUser(firstName, lastName, message='welcome my home'):
    return f'Hi {firstName} {lastName}! \n{message}' #\n new line satır başı yapar
#fonksiyonda işletilen bir işlemin çıktısını döndürmek için return kullanlır
#
greetinMessage = getGreetUser("Ayhan","Işık")
print(greetinMessage)


#pass es geçme komutudur programda henüz doldurmadığımız yerlerde kulllanılabilir
#pass hiçbirşey yapma anlamına geliyor program böylecce hata vermez
email = 'abcdefg@abcdef.com'
def validateEmail(email: str) -> bool:
    # kod yazarken daha okunaklı olması için fonksiyonun fonksiyonun tanımında geri  döneceği veri tipini ve alabileceği
    # argümanların tiplerini yazmak çok faydalıdır. emailimiz bir str idi yazdık geri verdiği değer ise bool onuda yazdık
    if email.count('@') != 1:
        return False
    numberOfDots = email.count('.', email.find('@'))
    #countun 2. parametresi bize istediğimiz noktadan sonra 1. paramtredeki ifade varmı diye arama yaptırdık
    #2. paramtreye girdiğimiz find @ gördüğü ilk paramtrei döndürecek
    if numberOfDots != 1:
        return False
    return True
if validateEmail(email):
    print("your email is valid")
else:
    print("your email is not valid")

