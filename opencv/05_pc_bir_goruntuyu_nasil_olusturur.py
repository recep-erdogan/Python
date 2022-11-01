import cv2
import numpy as np

#img = np.zeros((10,10,3), np.uint8) #renkli görüntü için 3 yazmıştık siyah beyaz için bir şey yazılmaz
img = np.zeros((10,10), np.uint8) #siyah beyaz oldu


img[0,0] = 255
img[0,1] = 155
img[0,2] = 75
img[0,3] = 25

""" img[0,0] = (255,255,255)        #bu şekilde pixelleri tek tek boyayabiliriz
img[0,1] = (255,255,155)
img[0,2] = (255,255,75)
img[0,3] = (255,255,0) """


img = cv2.resize(img, (1000,1000), interpolation=cv2.INTER_AREA)
#iterpolation yeniden boyutlandırıken bazı çakışmaların olmasını önler her resize fonsiyonunda kullanılabilir

cv2.imshow("Canvas",img)
cv2.waitKey(0)
cv2.destroyAllWindows()