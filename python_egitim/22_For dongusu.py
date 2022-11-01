sayi = range(5) #range belirli bir sayı aralığında sayyı dizisin oluşturur.burada sadece 5 girildiği için
#1,2,3,4 ü yazar yani bir eksik değere kadar.
index = 1
for index in range(1,10,2):#bir öneki uygulamadaki üçgen eklini yapalım
    #index döngünün değişkeni
    #range(1,10,2) 1 başlangıç sayyısı, 2 atlama sayısı 2 şer 2 şer artacak 10 son sayı 10 dahil değil
    #in range'in içindeki her bir sayıyı sırayla alarak index'e atıyor
    print(f"{'*' * index:^9}")
print("done")

for character in "Python":# strinlerde karakter listesi olduğu için aynı işlemi strinlerlede yapabiliriz
    print(character)

for item in ["Ali","Veli","Ferhat"]:# doğrudan listelerle de kullanılabilir.
    print(item)

#önce tek çift sayıları ayıran kodu yazdık, sonrasında tekleri ve çiftleri kendi iinde toplayan kodu yazdık
numbers = [13,12,31,14,51,9,12,15,65,64,92,6,16,19]
evenNumbersTotal = 0
oddNumbersTotal = 0
for number in numbers:
    if number % 2 == 0:
        print(f"Number{number} is an even number.")
        evenNumbersTotal += number
    else:
        print(f"Number{number} is an odd number.")
        oddNumbersTotal += number
print(f"Total evven numbers is {evenNumbersTotal}")
print(f"Total odd numbers is {oddNumbersTotal}")

for outerIndex in range(1,6): #5-5 lik çarpım tablosu
    if outerIndex == 3:
        continue
    for innerIndex in range(1,6):
        if innerIndex == 3:
            continue # 3lerle çarpımların satırını es geçmek için kullandık
            #continue bu adımı es geç ve döngünün başına dön demek break komple döngüyü kırıyor
        print(f"{outerIndex * innerIndex:4}", end='')
        # normalde printte vasayılan olan newline komutu yerine hiçbir şey koyma dedik
        #f stringlede değeri 4 karaktere boşlukla tamamlattırdık
    print() #boş print satır atlamaya yarıyor