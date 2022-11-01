import cv2

cap = cv2.VideoCapture(0)# fonksiyonun parametresi 0 ise webcami açarak görüntü alır, tırnak içinde dosya yolu
# aynı dizinde ise sadece adı yeterli ve dosya uzantısı yazılırarak var olan bi video çalıştırılabilir

while True: #videonun uzunluğu boyunca tüm kareleri işleyebilmesi için sonsuz döngü kurduk
    ret, frame = cap.read()#bu fonksiyon 2 değer döndürür görseli doğru okuduysa true yanlış ise false 2. ise kareker
    if red == 0:
        break # özellikle hazır videolarla çalışılırken yeni kare gelmediğinde red değeri 0 olur. bu if bloğunu -
        #yazmazsak video bittiğinde program hata döndürür
    frame =cv2.flip(frame,1)#bu fonsiyon görütüyü aynalar. 1.parametre ters çevirelecek görsel 2.si ise eksen 1 y ekseni
    cv2.imshow("Webcam",frame)
    #cv2.waitKey(30) # herbir kareyi 30ms beklettirdik bu süre artarsa çok donuk bir görüntü gelir 0 olursa tek bir kare olur
    #waitkeyi if ile kullanmak daha iyi olur q tuşuna basılırsa çıkış yapan kod aşağıdaki gibi olur
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
