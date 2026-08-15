import cv2

img = cv2.imread(r"C:\Tanjiro.jpg")

if img is None:
    print("Image not found!")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    result = cv2.Canny(gray, 100, 200)
    
    cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Canny Outline", cv2.WINDOW_NORMAL)
    
    cv2.imshow("Original Image", img)
    cv2.imshow("Canny Outline", result)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
