import cv2

img=cv2.imread(r"C:\Tanjiro.jpg",0)

edges=cv2.Canny(img,100,200)

cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.namedWindow("Canny Edge", cv2.WINDOW_NORMAL)

cv2.imshow("Original",img)
cv2.imshow("Canny Edge",edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
