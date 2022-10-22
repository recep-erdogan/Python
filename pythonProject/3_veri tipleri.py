smpleInteger = 123
print(smpleInteger)
print(type(smpleInteger)) # syi değişkeinin tipini yazdırdık

sampleBinary = 0b1010 #0b den sonra ikilik karşılığını bildiğimiz sayıyı integera dönüştürür
print(sampleBinary) #b nin küçük yada büyük olması fark etmez
sampleBinary = 0B1010
print(sampleBinary)

sampleOctave = 0o543# oktav sayılarda (sekizlik) o kullanılır
print(sampleOctave)
sampleOctave = 0O543 # o'nun büyük küçük olması yine fark etmez
print(sampleOctave)

sampleHexadecimal = 0x2F3 #16 lık sayıları integera dönüştürdük x büyük küçük farketmez aynı şekilde f de fark etmez
print(sampleHexadecimal)

sampleFloat = 4.2 #ondalıklı sayılar floattır
print(type(sampleFloat))

sampleBigFloat = 1.8e23#uzun bir sayının örnek bilimsel gösterimi e büyük veya küçük olabilir e= exponansiyelden gelir
print(sampleBigFloat)
sampleSmallFloat = 2.3E-54
print(sampleSmallFloat)
print(type(sampleSmallFloat))

sampleString = "This is \"stupid\" example for printing "
#normalde çift tırnak içinde çift tırnak kullanınca problem olurdu ters slaş ile birlikte kullanılırsa bu sorun olmaz
sampleString += "\'\x61\', \'\xAE\' and \'\uA7B5\' characters"
# \x heksadesimal sayı belirtir 61 bir onaltılık sayıyımış. \u ise uni kodu girilen ifadeyi yazdırmada kullanıldı
#bu şekilde klavyede olmayan semboller bastırılabilir. character map diye aratınca bütün semboller bulunabilir
sampleString += "\t because it is for presenting escape sequence"
#\t ise bir tab boşluğu bırakmak için kullanılır
