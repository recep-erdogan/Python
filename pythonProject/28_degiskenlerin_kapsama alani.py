message = "c" #programın n başında tanımlanan bu değiken bütün programı kapsar, fonksiyonların içi, dışı

def greet(name):
    massage = "a"
#print(name) #print(massage) bu şekilde yazdığımızda name error alırız.
#çünkü her iki değişkende lokal değişkenlerdir.

def senMail(name):
    massage = "b"
    #buradaki massage ve name değişkeleri isim olarak önceki fonksiyonla aynı olsa da lokal deeğişkenler olduğu için
    #tamamen farklıdırlar

    #fonksyonlardaki bu gibi değikenler çağırıldıkları çok kısa bi süre için hafızada bulunur daha sonrasında
    #garbage collector yani çöp toplatyıcı tarafından tekrar hafızadan silinir.

    #programın başında tanaımladığımız message değişkeni garbage collector tarafından daha geç silinir bundan dolayı
    #çok fazla global değişken kullanmamak önemlidir,global değişkenleri çok kullanmak pek çok soruna sebep olabilir.

greet("ferhat")
print(message) #greet fonksiyonunu çağırmamıza rağmen terminale ilk başktaki değişkenzin değerini bastı
#fonksiyonun içindeki değişken ismi aynıda olsada ikisinide ayrı değişken olarak ele alıp işletiyor
#fonksiyon içindeki lokal diğeri ise global değişken, ikisinin hafızada yer ettiği yerler farklı
#foknsiyonun içindeki message değişkeinin de diğeri gibi global değeriyle aynı olduğunu bildirip, global
#değişkeninin değişmesini sağlayabliriz fakat bu hiç tavsiye edilen bir opsiyon değildir.
def greet(name):
    global massage
    massage = "a"

    #yeni sayfa
if True:
    massage = "c"
#if ve döngü komutları içindeki değişkenler pythonda kapsama alanı bulunmuyor, c ve avada ise tam tersi
# yeni saydada daha öncesinde herhangibir yerde message değişeni tanılanmamış olsada if bloğu içinde
# massgage değişkeni global bir değişken olarak varsayılır ve hata vermez

def greet(name):
    global massage
    massage = "a"

def sendmail(name):
    message = "b"

#yeni sayfa
import random
characters = 'asdasfadcklsfdsjfdlşdfg!^+"&%'
password = ""
for i in range(8):
    password += random.choice(characters)
print(password)
# password değişkeni for döngüsü içinde fakat ayrı bir kapsama alanına sahip değil, döngü içindede global değişken
#olarrak işletiliyor


from random import choice, randint
"""bu şekilde random kütüphanesinden sadece choice komutu eklenmiş oldu
bu şekilde çağırdığmızda modülün ismini(choice) ve ardından nokta(.) koymamıza gerek yok('random.' bunu sildik)
kütüphane ekleme kısmında virgül atarak bir başka komutu daha ekleyebiliriz (, randit)"""

characters = 'asdasfadcklsfdsjfdlşdfg!^+"&%'
password = ""
for i in range(randint(8, 16)): # randit ile şifre uzunluğunuda rastgele belirledik 8 ile 16 arası rastgele oldu
    password += choice(characters)
print(password)
# password değişkeni for döngüsü içinde fakat ayrı bir kapsama alanına sahip değil, döngü içindede global değişken
#olarrak işletiliyor


#yeni sayfa
from random import choice, randint

characters = 'asdasfadcklsfdsjfdlşdfg!^+"&%'

password = choice(characters)
print(password)

def choice(sample: str) -> str:
    return 'F'
"""dosyamıza bir fonksiyon eklediğimizde ve aynı ismi taşıyan başka bir fonksiyon bizim programımızda tanımlıysa
dışarıdan ekledğimiz fnksiyon çalışmaz, bizim içere tanımladığımıız fonksiyon çalışır. bizim yazdığımız fonksiyona
kadar çağrılan fonksiyon işletilir, çalışma sırası bizim fonksiyonumuza geldiği andan itibaren bizim fonsiyonumuz
işletilir"""


password = ""
for i in range(randint(8, 16)): # randit ile şifre uzunluğunuda rastgele belirledik 8 ile 16 arası rastgele oldu
    password += choice(characters)
print(password)