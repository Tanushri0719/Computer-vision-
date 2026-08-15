import cv2

img = cv2.imread(r"C:\Tanjiro.jpg")

watermark = img.copy()

cv2.putText(watermark,"TANJIRO",(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.namedWindow("Watermarked Image", cv2.WINDOW_NORMAL)

cv2.imshow("Original",img)
cv2.imshow("Watermarked Image",watermark)

cv2.waitKey(0)
cv2.destroyAllWindows()
