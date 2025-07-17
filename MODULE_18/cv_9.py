import cv2 

img = cv2.imread('image.jpg')

resized = cv2.resize(img, (640, 640))

ksize = (7 , 7)

sigmaX = 0
sigmaY = 0 

blur = cv2.GaussianBlur(resized, ksize, sigmaX, sigmaY)

cv2.imshow('input', resized)
cv2.imshow('blurred', blur)

cv2.waitKey(0)
cv2.destroyAllWindows()