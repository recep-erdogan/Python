# kullanıcı adını girsin ismi 3'den kısa veya 15'den uzunsa hata mesajı yazdırsın ve tekrar ismini istesin
#geçerli bir isim alana kadar veya kullanıcı quit yazıncaya kadar sürekli sorsun
#geçerli bir isim girince program merhaba desin

while True:
    name = input("hi What is your name? ")
    if len(name) < 3 or len(name) > 15:
        print("pleese enter true name ")
    elif name.lower() == "quit":
        break
    else:
        print(f'hi {name}')
        break