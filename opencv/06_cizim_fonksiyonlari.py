import cv2
import numpy as np


canvas = np.zeros((512,512,3),dtype = np.uint8) +200

cv2.line(canvas,(50,50),(512,512),(255,0,0),thickness=5)#çizim yapılacak tuval, çizginin başlama noktası,-
#çizgini bitiş noktası,rgb renk kodu, çizgi kalınlığı thickness yazmadan sadece 5 de yazılabilirdi

cv2.rectangle(canvas,(20,20),(50,50),(0,255,0),7) #kalınlık parametresine -1 girilirse içi dolu olur

cv2.circle(canvas,(250,250),100,(0,0,255),5) # çemberde merkez nokta ve yarıçap değeri giriliyor,içi dolu olsun
# -#istenir ise kalınlık parametresi -1 yazılmalı

#üçgen çizmej için üç tane çakışan line fonksiyonu kullanılabilir

points = np.array([[[120,200] ,[330,200], [290,220], [220,250]]],np.int32)
cv2.polylines(canvas, [points], True,(0,0,100),5) #çok çizgili çizim için bu fonksiyon kullanır, çizilen şeklin kapalı-
#olması için true girildi

cv2.ellipse(canvas,(300,300),(80,20),10,90,360,(255,255,0),-1)#sırasıyla parametreler üstüne çizim yapılan tuval, merkez noktasının kordinatı -
#genişlik ve yüksekliği, yatay eksenle yapacağı açı, kaç dereceden kaç derecen başlayacağı, kaç derecede biteceği, -
#renk, kalınlık bilgisi



cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindiw()