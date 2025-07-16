import cv2

img = cv2.imread('image.jpg')

row = img.shape[1]
column = img.shape[0]

center = (row // 2, column // 2)
angle = 90

r = cv2.getRotationMatrix2D(center, angle, 1.0)

img_rotated = cv2.warpAffine(img, r, (row, column))


cv2.imshow('Original Image', img)
cv2.imshow('Rotated Image', img_rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()