import cv2

img = cv2.imread('./sample/data/lena.jpg', 0)

cv2.imshow('Lena', img)

escKey = 27

key = cv2.waitKey(0)

if key == escKey:
  cv2.destroyAllWindows()
