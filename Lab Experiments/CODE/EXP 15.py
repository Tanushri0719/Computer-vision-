import cv2
import numpy as np

img=cv2.imread(r"C:\Tanjiro.jpg")

rows,cols=img.shape[:2]

src=np.float32([[50,50],[300,50],[50,300],[300,300]])
dst=np.float32([[10,100],[290,40],[80,290],[320,320]])

H=cv2.getPerspectiveTransform(src,dst)
out=cv2.warpPerspective(img,H,(cols,rows))

cv2.imshow("Original",img)
cv2.imshow("DLT",out)

cv2.waitKey(0)
cv2.destroyAllWindows()
