tempreture = float(input("Sıcaklığı giriniz: "))

ishot = input("hava sıcak mı? (E/H) ")
if ishot.lower() == "e":
    ishot = True
    isCold = False
elif ishot.lower() == "h":
    ishot == False
else:
    print("geçerli bir giriş yapmadınız")

isCold = input("Hava soğuk mu?(E/H) ").lower()
if isCold.lower() == "e":
    isCold = True
    ishot = False
elif isCold.lower() == "h":
    isCold = False
else:
    print("geçerli bir giriş yapmadınız ")

isSnowy = input("Hava Karlı mı?(E/H) ").lower()
if isSnowy.lower() == "e":
    isSnowy = True
elif isSnowy.lower() == "h":
    isSnowy = False
else:
    print("geçerli bir giriş yapmadınız ")

isRainy = input("Hava yağmurlu mu?(E/H) ").lower()
if isRainy.lower() == "e":
    isRainy = True
elif isRainy.lower() == "h":
    isRainy = False
else:
    print("geçerli bir giriş yapmadınız ")



if tempreture >= 30:
    ishot = True
    isCold = False
elif tempreture <= 10:
    isCold = True
    ishot = False

if tempreture < 4 and isRainy:
    isSnowy = True

if ishot and isRainy:
    # and bloğu ile iki şart sağlanıyorsa bloğun içine girer
    print("sıcak ve yağmurlu bir gün")
elif ishot and not isRainy:
    #not sonuç true değilse true sonucu verir
    print("sıcak bir gün")
elif isCold and isSnowy:
    print("havada beq güzelimiş soğukcana ve karlı bir gün")
elif isCold and not isSnowy:
    print("kuru ayaz")
else:
    print("standart bir gün")
    if tempreture == 25 and not isRainy:
        print("müthiş bir gün")
    elif tempreture != 25 and not isRainy:
        print("ılık bir gün")
    else:
        print("yağmurlu bir gün")

if isSnowy or isRainy:
    print("yollar kaygan dikkatli sür!")
print("günün enjoy olsun")