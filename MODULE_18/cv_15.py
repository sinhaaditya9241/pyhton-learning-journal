import cv2

cap = cv2.VideoCapture(0)

while cap.isOpened():
    _, frame = cap.read()
    cv2.imshow("Webcam Feed", frame)

    if cv2.waitKey(10) == ord('q'):
        break


cv2.destroyAllWindows()