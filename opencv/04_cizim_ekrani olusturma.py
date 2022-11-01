import cv2
import numpy as np

canvas = np.zeros((512,512,3),dtype = np.uint8) +130# 512x512 lik bir siyah arka plan oluşturduk bunu +255 ile beyaz yaptık
#3 kanllı, dtype np.uint8 çizim yaptığımızda kullandığımız veri tipi
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindiw()