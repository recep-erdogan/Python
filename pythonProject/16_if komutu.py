ishot = True
isCold = False
isSnowy = True
isRainy = False

if ishot:
    #ifden sonra gelen ifade blooen True değerini alıyorsa if bloğunun içi çalışır
    print("sıcak bir gün")
    #if girinisi dışında olan kodlar if bloğundan bağımsız çalışır
        if isRainy:
            print("yağmurlu bir gün")
elif isCold:
    print("havada beq güzelimiş soğukcana")
        if isSnowy:
            print("karlı bir gün")
else:
    print("günün enjoy olsun")
    #iç içe if blokları kullanılabilir bir tab boşluk bıakılması gerekiyor.
    #bir tab 8 space boşluktan oluşuyor