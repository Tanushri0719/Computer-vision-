import cv2

img = cv2.imread(r"C:\Tanjiro.jpg")

if img is None:
    print("Image not found!")
else:
    result = cv2.GaussianBlur(img, (15, 15), 0)
    
    cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Gaussian Blur", cv2.WINDOW_NORMAL)
    
    cv2.imshow("Original Image", img)
    cv2.imshow("Gaussian Blur", result)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
