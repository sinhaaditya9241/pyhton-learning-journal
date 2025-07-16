import cv2

img = cv2.imread('image.jpg')

width = 450
height = 550
dim = (width, height)

resized = cv2.resize(img, dim)
print('Image shape:', resized.size)
cv2.imshow('original', resized)

#flip = cv2.flip(resized, 1)
#cv2.imshow('Horizontal', flip)

#flip_1 = cv2.flip(resized, 0)
#cv2.imshow('Vertical', flip_1)

flip_2 = cv2.flip(resized, -1)
cv2.imshow('horizotal and vertical', flip_2)

cv2.waitKey(0)
cv2.destroyAllWindows()