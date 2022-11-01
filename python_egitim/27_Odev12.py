"""Bir stringin polindrom olup olmadığını kontrol edecek program. polindrom tersindende okunduğunda aynı
şekilde okunana kelimelerdir (örn nalan, nazan radar)"""

def polindrom(kelime: str) -> bool:
    terskelime = kelime[::-1]
    if kelime == terskelime:
        return True
    else:
        return False

if polindrom("nazan"):
    print("1)kelime polindrom!")
else:
    print("1)kelime polindrom değil")


#hocanın yazdığı porgram
def isPolindrome(string: str) -> bool:
    reverse = ""
    for character in string:
        reverse = character + reverse
        #kelimei ters çevirdik
    if string == reverse:
        return True
    return False
string = "nalann"
if isPolindrome(string):
    print(f"2){string} is a polindrome string.")
else:
    print(f"2){string} is not a polindrome string.")

#hocanın 2. kodu
"""strinlerde üç paramere bulunuyor 1. parametre başlagıç noktası 2. parametre bitiş noktası 3. parametre ise
1. ve 2. paramtereki aralıktaki sayıları kaç adımda seçmesi gerektiğini verir 
örn. strin[1,10,2] 1.karakteri seç sonra 3.yü seç sonra 5. sonra 7.
 reverse etmek için [::-1] 1.parametreye : yazınca stringin başından başlar 2. paratmetreye : yazınca sonuna kadar gider
 ve 3. paramtreye -1 yazınca terse doğru birer birer ilerler."""
def isPolindrome(string: str) -> bool:
    reverse = string[::-1]
    if string == reverse:
        return True
    return False
string = "nalan"
if isPolindrome(string):
    print(f"3){string} is a polindrome string.")
else:
    print(f"3){string} is not a polindrome string.")