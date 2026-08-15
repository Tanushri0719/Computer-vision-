import cv2
import numpy as np

img = cv2.imread(r"C:\Tanjiro.jpg")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sobelx = cv2.Sobel(gray,cv2.CV_64F,1,0,3)

sobely = cv2.Sobel(gray,cv2.CV_64F,0,1,3)

gradient = cv2.magnitude(sobelx,sobely)

gradient = np.uint8(gradient)

cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.namedWindow("Gradient Mask", cv2.WINDOW_NORMAL)

cv2.imshow("Original",img)
cv2.imshow("Gradient Mask",gradient)

cv2.waitKey(0)
cv2.destroyAllWindows()
