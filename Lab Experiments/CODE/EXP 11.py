import cv2
import numpy as np

image = cv2.imread(r"C:\Tanjiro.jpg")

if image is None:
    print("Image not found!")
else:
    height, width = image.shape[:2]
    
    points1 = np.float32([[0, 0], [width - 1, 0], [0, height - 1]])
    points2 = np.float32([[0, height * 0.1], [width * 0.85, height * 0.2], [width * 0.15, height * 0.7]])
    
    matrix = cv2.getAffineTransform(points1, points2)
    affine_image = cv2.warpAffine(image, matrix, (width, height))
    
    cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Affine Transformation", cv2.WINDOW_NORMAL)
    
    cv2.imshow("Original", image)
    cv2.imshow("Affine Transformation", affine_image)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
