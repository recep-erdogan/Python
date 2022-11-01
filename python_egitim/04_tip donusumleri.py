"""input fonksiyonu ile alınan sayıların türleri varsayılan olarak stringtir, bir integer değer ile aritmatik işlem
yapılabilmesi için öncelikle bu tip dönüşümü yapılması lazım"""
birthYear = input("Enter birth year: ")
age = 2022 - int(birthYear) #sadece buradki işleme özel türü değiştirldi normal şartlarda türü yine str
print(type(age))
print("yoru age is",age)
#benzer şekilde float ve bool fonksiyonlarıda kullanılabilir
sampleFloat = float(input("Enter a Float: "))
print(type(sampleFloat))
print(sampleFloat)