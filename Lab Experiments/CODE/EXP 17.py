import cv2

img=cv2.imread(r"C:\Tanjiro.jpg",0)

sobelx=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)

cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.namedWindow("Sobel X", cv2.WINDOW_NORMAL)

cv2.imshow("Original",img)
cv2.imshow("Sobel X",cv2.convertScaleAbs(sobelx))

cv2.waitKey(0)
cv2.destroyAllWindows()
