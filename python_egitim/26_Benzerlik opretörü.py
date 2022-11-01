# nesne tabanlı yazılımda her bir nesnenin bilgisayda bir hafızası vardır. her bir nesnenin kendie ait
# adresi vardır bu adress o nesnenin kimliğidir. program içinde kaç yerde kullanırsak kullanalım bu adres aynıdır
print("1)",id(1000))

string1 = "Ferhat"
print("2)",id(string1)) #string1 ve string2 'nin id'leri aynı
string2 = "Ferhat"
print("3)",id(string2))
# C# da her değişken başka bir nesne ama pythonda değer bir nesne oluyor değişkenlerin id leri olmuyor
#değişkenler nesnelere işaret eden varlıklardır. Ferhat bir nesne iken string1 ve string2 değildir.
#Pythonda kimlikler kullandığımız an oluşur ve program çalıştığı sürece aynı kalır. program tekrar çalıştırılınca değişir.
#komplex nesnelerin içerikleri aynı olsa bile idleri farklıdır listeler kümeler ve demetler konusunda ele alıncak
if id(string1) == id(string2):
    print("4) They have same identity")
#Nesneleri karşılaştırırken gerçekten aynı nesne olup olmadığını is ve isnot ifadeleri kullanılır.
if string1 is string2: # bir önceki ifle aynı işi yaptık
    print("5) They have same identity")
#is ve is not opertörlerini bir şeyin içinin boş olup olmadığını kontrol etmek için de kullanırız
# None içi boş anlamına geliyor C# da benzer olarak null vardır.
#pythonda None bir nesnedir, değeri yoktur , 0 değildir, boş bir string değildir, False de değildir

sampleVarieble = None
if sampleVarieble is None:
    print("6) Variable value is None")

def greetUser(firstName: str, lastName: str, message: str="Welcome my home") -> None:
#herbir fonksiyon girdisi için türlerini tek tek belirttik fakat bu fonsiyonun return ettiği bir değer yok
#bundan dolayı geri döndürdüğü kısma None yazdık.
    print(f'7) hi {firstName} {lastName}!')
    if message is not None:
# message kısmına eğer "" (çift tırnak içinde hiçbirşey yazmazsa) girilirse fonksyion mesaj yazdırırken bir satır atlar
#bunun olmasını istemiyorsa hiçbirşey girilmemişse şunu yap diyerek bir if komutu yazdık
#hehangi birşey girilmezse varsayılan değeri yazdırılır
     print(message)
greetUser('Ahmet','Yılmaz')

#pythonda None bir nesnedir, değeri yoktur , 0 değildir, boş bir string değildir, False de değildir, bir idsi vardır !
password = ""
if password is "":
    print("8) Password is not be empty")
#passwordün idsi boşluğun idsi ile aynı mı? evet aynı mesajı terminale yazar
if password is None:
    print("9) Password is not be empty")
#burda ise terminale bi şey yazdırmaz çünkü None'ın ile Password'un idsi eşit değildir
#Passwordun idsi program çalıştırıldığında oluşturuldu None'ın idsi ise program çalışmaan önce zaten belliydi
#özetle nesnelerin aynı olup olmadığını karşılaştırmak için is ve is not operetörlerini kullanılırız
#değerlerini karşılaştırmak içinse mantık oopertörlerini kullanırız (== ,!= , >=, <=)

a = 1
b = 1
if id(a) == id(b): #a'nın idsi'nin değeriyle b'nin idsi'nin değerininin aynı olup olmadığı karşılaştırdık
    print('a is same as b')
if a is b: # burda ise yukardaki işleme benzsede sadece nesnelerin kiliklerinin aynı olup olmadığına bakıyor
    print('a is same as b')
#ilkinde değerleri karşılaştırdık, kkincide ise direkt nesnelri karşılaştırdık

variable1 = 1
variable2 = 2
# iki değişkenimizin değerlerini değiş tokuş ettirecek bir kod yazdık
print(f'variable1 = {variable1} variable2 = {variable2}')
temporary = variable1 #işlemi yapabilmek için geçici bir değişken tanımladık
variable1 = variable2
variable2 = temporary
print(f'variable1 = {variable1} variable2 = {variable2}')
#Bu programda iki değişkenin değeride integer bu iki eğişkenin değeri farklı olsa değeri farklı olan değişkenleri takas
#yapmamız gerekirdi bu yüzden bir if bloğu ekleyip tekrar yazalım

variable1 = 1
variable2 = '2'
if type(variable1) is type(variable2):
#type fonksiyonu tipi geri veriyor, tip ise bir nesnedir bundan dolayı is ile karşılaştırıyoruz
    print(f'variable1 = {variable1} variable2 = {variable2}')
    variable1, variable2 = variable2, variable1
#iki değişekenin değeri bu şekilde daha pratik bir yolla değiştirilebilir. Bu daha da uzun olabilirdi
#birinci değişkene birinci değer ikiciye ikinci değer ... sırasıyla atanır.
    print(f'variable1 = {variable1} variable2 = {variable2}')
else:
    print("Swapping is not applied")

