import cv2

cap = cv2.VideoCapture(0)

cv2.namedWindow("Normal Motion", cv2.WINDOW_NORMAL)
cv2.namedWindow("Slow Motion", cv2.WINDOW_NORMAL)
cv2.namedWindow("Fast Motion", cv2.WINDOW_NORMAL)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
        
    cv2.imshow("Normal Motion", frame)
    cv2.imshow("Slow Motion", frame)
    cv2.imshow("Fast Motion", frame)
    
    key = cv2.waitKey(25) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('s'):
        cv2.waitKey(100)
    elif key == ord('f'):
        cv2.waitKey(5)

cap.release()
cv2.destroyAllWindows()
