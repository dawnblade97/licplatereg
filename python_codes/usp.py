import cv2
import sys
 
img = cv2.imread(sys.argv[1], cv2.IMREAD_UNCHANGED)
 
print('Original Dimensions : ',img.shape)
 
scale_percent = 500 # percent of original size
width = int(416)
height = int(416)
dim = (width, height)
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
f=sys.argv[1]
cv2.imwrite(f,resized)
print('Resized Dimensions : ',resized.shape)
 
cv2.imshow("Resized image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows() 
