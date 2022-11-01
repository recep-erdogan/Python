#1
firstName = 'Atilla'
lastName = 'İlhan'
message = firstName + " [" + lastName + "] is a poet "
print("1)",message)

# bu işlemi bu kadar uzun bir şekilde yapmak yerine biçimli stringle daha kolayca yapabilirdik

#2
formattedMessage = f"{firstName} [{lastName}] is a poet" #f büyük veya küçük olabilir
#değişkenlerin değerlerini f{}'in içinde bulunduğu yerlere koyarak aynen yazdıracak
print("2)",formattedMessage)

#3
formattedMessage = f"{firstName:3} [{lastName:10}] is a poet"
#burada : dan sonraki sayı '3' firstname 3 karakterden küçükse onu 3'e tamamlar değilse dokunmaz.
#3 e tamamlarken boşluk kullanır fakat firstname 3 karakterden küçük olmadığı için herhangi bir şey yapaz
#fakat attillanın yanına 5 tane boşluk koyar
print("3)",formattedMessage)

#4
formattedMessage = f"{firstName:.2} [{lastName:.3}] is a poet"
#burada ise .2 firstnamedkeki ilk iki harfi al geri kalanı sil demek oluyor
print("4)",formattedMessage)

#5
formattedMessage = f"{firstName:10.2} [{lastName:10.3}] is a poet"
#burada ise önce ilk 2 harfini alır ve kalan metni 10 karekterli ifade olacak şekilde sağına boşluklar doldurdur
print("5)",formattedMessage)
formattedMessage = f"{firstName:10.10} [{lastName:10.10}] is a poet"
#genellikle bu şekilde kullanılır bu şu demek oluyor firstname 10 karakterden büyükse onu 10 karakter olacak şekilde
# kırp ve 10 karakterden küçükse onu boşluklar ekleyerek 10 karakterli yap


number1 = 3
number2 = 6
# satır yetmeyecek gibi olursa ters slaş ile alta geçilebilir.
print(f'6) {number1} plus {number2} is {number1 + number2} and is not \
{2 * (number1 + number2)}. ')
"""printte süslü parantezlerin içinde aritmatik işlem yapıldığında dönen sonuç tekrar stringe çevrilir ayrıca
bir değer oluşturup tek tek yazmaya gerek yok"""
#7
piNumber = 3.14159265359
print(f"7) {{Pi number}} is{{ {piNumber:.6}" #normalde çok daha uzun olan pi sayısının sadece ilk 6 rakamını aldık
      f" }} and its half is{piNumber/2:.6}")
#pi sayısını önce ikiye böldük daha sonra oluşan sayının ilk 6 rakamını aldık en sonki değer 0 oldç için onu yazmamış
# normal süslü parantezin haricinde süslü parantez yazdırmak istersek ekstra süslü parantez yazmamız gerek
#8
errorNo = 12345
print(f"8) there is a {errorNo:b} error!") #bu şekilde integer sayıyı binarye dönüştürüp  yazdırdık
#9
print(f"9) there is a {errorNo:#b} error!")
# aynı işlemde b nin önüne # işareti koyarsak ikilik karşılığının başına 0b ekleyerk terminale yazdırır
# # ile başalması ikilik sayının kod içindeki beyan şeklidir aynısı oktav vs sayılar için yapılabilir.

#10
print(f"10) there is a {errorNo:o} error!") # aynı işlemleri sekizlik (oktav) sayı için yaptık
#11
print(f"11) there is a {errorNo:#o} error!")
#12
print(f"12) there is a {errorNo:x} error!") # aynı işlem onaltılık sistem için yapıldı (hexadecimal)
#13
print(f"13) there is a {errorNo:#x} error!")
#14
print(f"14) there is a {errorNo:10x} error!") # 10 karaktere tamamlar sayının sonuna boşluk ekler
#15
#çok uzun sayıların kolay okunabilmesi için aralarına virgül konması iyi olur şu şekilde yapılır
number = 123123123123123123
print(f"15) sayının virgülle ayrılmış hali: {number:,}")

#bir metni sola sağa veya ortaya hizalamk istersek aşağıdaki adımları yaparız
message = "This is an example"
print(f"16) {message:<50}") #sola doğru yazıyı yaslar ve uzunluğunu 50 karekter olacak şekilde sağına boşluk ekler
print(f"17) {message:>30}")#sağa doğru hizalar ve uzunluğu 30 karakter olacak şekilde soluna boşluk ekler
print(f"18) {message:^40}")#ortaya hizalar ve uzunluğunu 40 karakter olacak şekilde sağdan ve soldan boşluk ekler
#aynı işlemleri boşluk yerine istediğimiz başka bir karekterle doldurabilirdik
print(f"19) {message:*<50}") #sola doğru yazıyı yaslar ve uzunluğunu 50 karekter olacak şekilde sağına boşluk ekler
print(f"20) {message:->30}")#sağa doğru hizalar ve uzunluğu 30 karakter olacak şekilde soluna boşluk ekler
print(f"21) {message:z^40}")#ortaya hizalar ve uzunluğunu 40 karakter olacak şekilde sağdan ve soldan boşluk ekler