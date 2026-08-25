import cv2

# Read image
img = cv2.imread(r"C:\Face.jpg")

# Create windows
cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
cv2.namedWindow("Extracted Object", cv2.WINDOW_NORMAL)

# Rectangle coordinates
x, y, w, h = 100, 80, 300, 250

# Draw rectangle
cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Extract object
object = img[y:y+h, x:x+w]

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Extracted Object", object)

cv2.waitKey(0)
cv2.destroyAllWindows()
