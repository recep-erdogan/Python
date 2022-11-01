import cv2
import numpy as np
import requests
url = "http://192.168.1.103:8080//shot.jpg"

while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content),dtype=np.uint8)
    #Görüntüleri bi array içinde tuttuk daha sonra bytearray'e çevirdik. aldığımız görünütleri önce depolayıp sonra-
    #tekrar hafızadan çekiyoruz
    img = cv2.imdecode(img_arr,cv2.IMREAD_COLOR)#1.parametre hafızadan aldığımız veriyi görünür hale getirir
    #2. parametre ise renkli görüntü almamızı sağladı -1 de yazsak aynı işi görürdü
    img =cv2.resize(img,(640,480)) # görüntüyü yeniden boyutlandırdık
    cv2.imshow("Android Camera",img)

    if cv2.waitKey(1) == 27: # önceden yaptığımız q ya basınca çıkan kodun kısa veriyonu imiş
        break
cv2.destroyAllWindows()
