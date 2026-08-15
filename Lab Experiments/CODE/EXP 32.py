import cv2
import numpy as np

img=cv2.imread(r"C:\Tanjiro.jpg",0)
kernel=np.ones((5,5),np.uint8)

closing=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)

cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.namedWindow("Closing", cv2.WINDOW_NORMAL)

cv2.imshow("Original",img)
cv2.imshow("Closing",closing)

cv2.waitKey(0)
cv2.destroyAllWindows()
