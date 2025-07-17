import cv2

img = cv2.imread('image.jpg')

resize = cv2.resize(img, (640, 480))

kernel = 3

blur = cv2.medianBlur(resize, kernel)

cv2.imshow('Blurred Image', blur)
cv2.imshow('Original Image', resize)

cv2.waitKey(0)
cv2.destroyAllWindows()