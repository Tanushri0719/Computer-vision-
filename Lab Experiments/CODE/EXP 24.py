import cv2

img = cv2.imread(r"C:\Tanjiro.jpg")

blur = cv2.GaussianBlur(img,(9,9),10)

mask = cv2.subtract(img,blur)

highboost = cv2.addWeighted(img,1.0,mask,2.0,0)

cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.namedWindow("High Boost", cv2.WINDOW_NORMAL)

cv2.imshow("Original",img)
cv2.imshow("High Boost",highboost)

cv2.waitKey(0)
cv2.destroyAllWindows()
