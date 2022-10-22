#program x harfleriyle azılmış F harfini terminale yazdırsın (for döngüsü ile)
deger1 = 5
deger2 = 2

for index1 in range(1,3):
    print("x" * deger1)
    for index2 in range(1,deger2):
        print("x" * 2)
        deger2 += 1
