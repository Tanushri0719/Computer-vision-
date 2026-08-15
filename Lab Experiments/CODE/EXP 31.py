import cv2
import numpy as np

img=cv2.imread(r"C:\Tanjiro.jpg",0)
kernel=np.ones((5,5),np.uint8)

opening=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)

cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.namedWindow("Opening", cv2.WINDOW_NORMAL)

cv2.imshow("Original",img)
cv2.imshow("Opening",opening)

cv2.waitKey(0)
cv2.destroyAllWindows()
