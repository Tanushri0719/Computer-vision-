import cv2

img=cv2.imread(r"C:\Tanjiro.jpg")

cv2.namedWindow("Object Recognition", cv2.WINDOW_NORMAL)

cv2.putText(img,"Tanjiro",(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

cv2.imshow("Object Recognition",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
