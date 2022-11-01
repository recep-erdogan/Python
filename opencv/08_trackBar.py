import cv2
import numpy as np

def nothing(x):
    pass #ilk iş olarak hiçbir işi olamyan bir fonksiyon tanımladık


img = np.zeros((512,512,3), np.uint8) #bi tuval oluşturduk
cv2.namedWindow("image") # pencereye bi ad verdik trackbar oluşturma esnasında burayı fonksiyona belirtebilmemiz lazım

#trackbarın oluşturulması
cv2.createTrackbar("R","image",0,255,nothing)
#parametreler sırrayla; kızağın adı, yerleşeceği penerinin adı, başlangıç ve bitiş değer aralığı
#nothing fonksiyonu ise opencv 'nin creat bar için kurduğu çölışma şeklinden ötürü
#aynı şekilde diğer renkler için de barlar oluşturalım
cv2.createTrackbar("G","image",0,255,nothing)
cv2.createTrackbar("B","image",0,255,nothing)
switch = "0: OFF, 1: ON"
cv2.createTrackbar(switch,"image",0,1,nothing) # on off butonu
cv2.createTrackbar("B","image",0,255,nothing)
#buraya kadarki kısım tasarımıydı bunun çalışabilmesi için trackbarların pozisyon verilerini çekmemiz lazım
#ve bunu anlık olarak yapmamız sürekli denetlememiz lazım o yüzden while döngüsü oluşturmalıyız

while True:
    cv2.imshow("image",img)
    if cv2.waitKey(1) & 0xFF == ord("q"): # q ya basınca kapanamasını ayarladık
        break
    #trackbarlardan verileri çekip değişkenlere atayalım
    r = cv2.getTrackbarPos("R","image")# ilk parametre trackbarın adı ikincisi pencere adı
    g = cv2.getTrackbarPos("G", "image")
    b = cv2.getTrackbarPos("B", "image")
    s = cv2.getTrackbarPos(switch,"image")

    if s==0:
        img[:] = [0,0,0] # swtich değeri 0 ise tüm pixel değerlerini 0 yapsın dedik

    if s == 1:
        img[:] = [b, g, r]
        # [:] diyerek img'nin tüm renk pixellerine erişim istediğimiz belirtiyoruz ve bunları sırasyıla b,g,r -
        # değerlerine eşitliyoruz


cv2.destrolAllwindows()