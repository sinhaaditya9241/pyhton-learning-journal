import cv2

video = cv2.VideoCapture('video.mp4')

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 25.0, (500, 760))

while video.isOpened():
    ret, frame = video.read()
    if ret:
        out.write(frame)
        cv2.imshow("Frame", frame)

   
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break


cv2.destroyAllWindows()        
