"""2020 yılından başlayarak 1900 yılına kadar olan artık yılları listele
artık yıllarr 4'e tam bölünen yıllardır.
100'e tam bölünen yılların arrtık yıl olabilimesi için 400'e tam bölünmesi gerekir örn 2000 yılı artık yıldır."""
year = 2020
liste = []
for i in range(121):
    if (year % 4) == 0 and (year % 100) != 0:
        #print("year: ",year)
        liste.append(year)
    elif (year % 100) == 0 and (year % 400) == 0:
        #print("year: ", year)
        liste.append(year)
    year -= 1
print(liste)