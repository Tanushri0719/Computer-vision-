import cv2
import numpy as np

image = cv2.imread(r"C:\Tanjiro.jpg")

kernel = np.ones((5,5), np.uint8)

dilate = cv2.dilate(image, kernel, iterations=1)

cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
cv2.namedWindow("Dilated Image", cv2.WINDOW_NORMAL)

cv2.imshow("Original Image", image)
cv2.imshow("Dilated Image", dilate)

cv2.waitKey(0)
cv2.destroyAllWindows()
