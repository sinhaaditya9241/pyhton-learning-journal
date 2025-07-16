import cv2

img = cv2.imread("image.jpg")

print("Dimensions:", img.shape)

width = 400
height = 1200
dim = (width, height)
resized = cv2.resize(img, dim)

cv2.imshow("window", resized)



cv2.waitKey(0)

cv2.destroyAllWindows()