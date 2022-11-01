#ikinci dereceden bir denklemin a,b ve c değerlerini alsın ve köklerini hesaplasın
import math
a = int(input("a sayısını giriniz: "))
b = int(input("b sayısını giriniz: "))
c = int(input("c sayısını giriniz: "))
delta = math.pow(b,2)-(4*a*c)
kok1 = (-b+delta**(1/2))/(2*a)
kok2 = (-b-delta**(1/2))/(2*a)
print(kok1)
print(kok2)