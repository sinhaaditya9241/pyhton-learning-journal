import cv2
import numpy as np

img = cv2.imread('bird_1.jpg', )

min_thresh = 100
max_thresh = 200

edges = cv2.Canny(img, min_thresh, max_thresh)

cv2.imshow('Canny Edges', edges)
cv2.imshow('Original Image', img)


cv2.waitKey(0)
cv2.destroyAllWindows()

