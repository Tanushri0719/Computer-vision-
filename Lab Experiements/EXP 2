import cv2

image = cv2.imread(r"C:\Users\Maruthi\OneDrive\Pictures\Screenshots\HOME..png")

blur = cv2.GaussianBlur(image, (15, 15), 0)

cv2.imshow("Original Image", image)
cv2.imshow("Blur Image", blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2

image = cv2.imread(r"C:\Users\Maruthi\Downloads\CLIMATE.png")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 100, 200)

cv2.imshow("Original Image", image)
cv2.imshow("Canny Edge Image", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
