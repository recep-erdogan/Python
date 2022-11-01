import cv2
import numpy

cv2.namedWindow("image",cv2.WINDOW_NORMAL) # 1.parametre peccere adı, 2. parametre pencereyi boyutlandırma
img = cv2.imread("clone.jpg",0) # 2.parametre 0 olunca gri tonlarla çalışır. 1. parametre için -
# eğer görüntü kod ile aynı dizinde değilse dosya yolu \clone.jpg ile yapılabilirdi
cv2.imshow("image",img) #1. parametre pencerinin adı ikincisi görünütünün saklı olduğu  değişken
cv2.imwrite(clone1.jpg,img)#1. parametrede belli bi dosya uzantısını da girip istdiğimiz adrese kaydedebiliriz
cv2.waitKey(0) # milisaniye cinsinden değer alır 0 girilirse herhangi bi tuşa basana kadar görsel ekranda görüntülenir
cv2.destroyAllWindows()





