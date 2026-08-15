import cv2

image = cv2.imread(r"C:\Tanjiro.jpg")

if image is None:
    print("Image not found!")
else:
    bigger = cv2.resize(image, (0, 0), fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)
    smaller = cv2.resize(image, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    
    cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Bigger Size", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Smaller Size", cv2.WINDOW_NORMAL)
    
    cv2.imshow("Original", image)
    cv2.imshow("Bigger Size", bigger)
    cv2.imshow("Smaller Size", smaller)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
