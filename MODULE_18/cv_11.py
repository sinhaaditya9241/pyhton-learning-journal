import cv2

img = cv2.imread('bird_1.jpg')

resize = cv2.resize(img, (520, 520))

d= 7

sigmaColor = 100
sigmaSpace = 100

b= cv2.bilateralFilter(resize, d, sigmaColor, sigmaSpace)

cv2.imshow('Bilateral Filtered Image', b)
cv2.imshow('Resized Image', resize)

cv2.waitKey(0)
cv2.destroyAllWindows()