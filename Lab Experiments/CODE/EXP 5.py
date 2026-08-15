import cv2
import numpy as np

image = cv2.imread(r"C:\Tanjiro.jpg")

kernel = np.ones((5,5), np.uint8)

erode = cv2.erode(image, kernel, iterations=1)

cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
cv2.namedWindow("Eroded Image", cv2.WINDOW_NORMAL)

cv2.imshow("Original Image", image)
cv2.imshow("Eroded Image", erode)

cv2.waitKey(0)
cv2.destroyAllWindows()
