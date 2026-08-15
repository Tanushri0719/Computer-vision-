import cv2

cap=cv2.VideoCapture(r"D:\Video.mp4")
frames=[]

while True:
    ret,frame=cap.read()
    if not ret:
        break
    frames.append(frame)
cap.release()

cv2.namedWindow("Reverse Video", cv2.WINDOW_NORMAL)

for frame in frames[::-1]:
    cv2.imshow("Reverse Video",frame)
    if cv2.waitKey(30)&0xFF==27:
        break
        
cv2.destroyAllWindows()
