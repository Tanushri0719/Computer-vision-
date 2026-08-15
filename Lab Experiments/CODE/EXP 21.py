import cv2
import numpy as np

img = cv2.imread(r"C:\Tanjiro.jpg")

kernel = np.array([[-1,-1,-1],
                   [-1,8,-1],
                   [-1,-1,-1]])

lap = cv2.filter2D(img,-1,kernel)

sharp = cv2.add(img,lap)

cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.namedWindow("Laplacian Sharpening", cv2.WINDOW_NORMAL)

cv2.imshow("Original",img)
cv2.imshow("Laplacian Sharpening",sharp)

cv2.waitKey(0)
cv2.destroyAllWindows()
