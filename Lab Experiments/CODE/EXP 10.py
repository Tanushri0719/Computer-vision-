import cv2
import numpy as np

image = cv2.imread(r"C:\Tanjiro.jpg")

if image is None:
    print("Image not found!")
else:
    matrix = np.float32([[1, 0, 150], [0, 1, 70]])
    height, width = image.shape[:2]
    moved_image = cv2.warpAffine(image, matrix, (width, height))
    
    cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Moved Image", cv2.WINDOW_NORMAL)
    
    cv2.imshow("Original", image)
    cv2.imshow("Moved Image", moved_image)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
