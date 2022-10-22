# yüksekliği 4  yarıçapı 6 olan silindirn hacmini hesaplayan program
import math

h = float(input("Silindirin yüksekliğini giriniz: "))
r = float(input("Silindirin yarıçapını giriniz: "))
hacim = round(math.pi * math.pow(r,2) * h)
print(f"Silindirin yarıçapı: {r} yüksekliği: {h} hacmi: {hacim}")
