#print() fonksiyonu

print("hello world")
print('hello world')# çift tırnak veya tek tırnak arasında burada bir fark yok
print("hello"+" "+"world")
print('hello' + ' ' + 'world')#string ifadeler birbiriyle toplanabilir
print('*' *10) #string değerler integer değerler ile çarpılabilir sonuç olarak yan yana 10 tane * olur
sempleString="hello world"
print(sempleString[6])#stringin 6. indisindeki harfi yazdırdık
print(sempleString[-1])# -1 girildiğinde en sondaki ifadeyi verir 0. indis 'h' geriye doğru sondan geliyor -2 dersek 'l'
print(sempleString[0:3])#0.indisten 3. indise kadarki harfleri yazdırır 3. indis dahil değil
print(sempleString[:3])#üst satırtadi kodla aynı işi yapar başa 0 girilmese bile varsayılan olarak 0 değeri kullanılır
print(sempleString[0:])#iknici inis boş bırakılırsa sonuna kadarki tüm harfleri yazdırır
print(sempleString[:])# her iki index de boş bırakılrsa baştan son tümünü yazdırır yine
print(sempleString[1:-2])#baştan birinci indexle sondan 2. karatere kadar yazar = ello wor

sempleString1="hello"
sempleString2=" "
sempleString3="world"
print(sempleString1 + sempleString2 + sempleString3) # önce değişkene atayııp sonra topşanırsa da aynı sonucu verir
print(sempleString1 , sempleString2 , sempleString3) # bu şekilde yazılığında arada pek çok gereksiz boşluk oluştu
""" bu şekilde virgül ile ayırnca otomatik araya bir boşluk koyarak birleştiriyor + ile yanyana yazıyor bu kullanımda
virgülün varsayılan değeri boşluk olduğu için bunu yapıyor bunu değiştirebiliriz bunu da ayrçala yaparız ayraç= sep"""
print(sempleString1 , sempleString2 , sempleString3, sep='')
# burda sep='' diyerek varsayılan değerini hiçbirşey yaptık başak ayraçlarda tanımlanabilir
print(sempleString1 , sempleString2 , sempleString3, sep=' *** ')
""" printle yazdırılacak şeyin içerisinde tek tırnak veya çift tırnak gösterilmesi istenirse ikisini birden uygun
bir şekilde yazmak lazım"""
sempleString4 = "'world'"
print(sempleString1,sempleString4)
sempleString4 = '"world"'
print(sempleString1,sempleString4)

# terminale birden çok satırlı bir şey yazdırmak istersek şu şekilde yaparız
sempleString="""Python's name does not come from a
 'snake'"""
print(sempleString)# yazdırılığı zaman 'snake' i aşağı yazdırdı.çift tırnakların yerine tek tırnaklarda kullanılabilirdi

#input() fonksiyonu
input("what is your name? ")# içerisinde kulanıcıya gösteriği mesajdan sonra bir giirdi için bekler ve aldığı cevabı
#geçici hafızasında saklar bu veriyi bir değişkene atayarak sakalamak anlamlı olur
name = input("what is your name? ")# sonuna konulan boşluk kullanıcının cevabının daha net gözükmesi için önemli
print('hi',name)