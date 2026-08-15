import cv2

image = cv2.imread(r"C:\Tanjiro.jpg")

if image is None:
    print("Image not found!")
else:
    clockwise = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    counterclockwise = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
    
    cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Clockwise", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Counter", cv2.WINDOW_NORMAL)
    
    cv2.imshow("Original", image)
    cv2.imshow("Clockwise", clockwise)
    cv2.imshow("Counter", counterclockwise)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
