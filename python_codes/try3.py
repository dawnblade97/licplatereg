import cv2
import numpy as np
import pytesseract
import sys
from PIL import Image

SCREEN_WIDTH = 128
SCREEN_HEIGHT = 64

f=open("log.txt","r")

f1=f.readlines()
ar=[str(x) for x in range (0,10)]
co_od=[]
for x in f1:
	if x[0] in ar:
		temp=[]
		for i in x.split(','):
			temp.append(int(i.strip(' ').strip('\n')))
		co_od.append(temp)

f.close()




img1=cv2.imread("/home/dawnblade/darknet/"+sys.argv[1])
c=0
for i in co_od:
	#315, 307, 425, 261
	crop_img=img1[i[3]:i[1],i[0]:i[2]].copy()


	img = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
	if img is None:
		print("Reading image from file {} failed.".format(inFile))
		exit(1)

	scale_factor = 6
	h, w = img.shape[:2]
	scaled_img = cv2.resize(img[0:h, 10:w], (0,0), fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_CUBIC)
	cv2.imshow("gg",scaled_img)
	cv2.waitKey(0)
	assert(scaled_img is not None)

	thres,thres_img = cv2.threshold(scaled_img, 0, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
	kernel = np.ones((1, 1), np.uint8)
	thres_img = cv2.dilate(thres_img, kernel, iterations=1)
	thres_img = cv2.erode(thres_img, kernel, iterations=1)
	thres_img=cv2.medianBlur(thres_img, 3)
	#thres_img = cv2.Canny(thres_img, 50, 150, apertureSize=3)
	

	se = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))
	thres_img = cv2.morphologyEx(thres_img, cv2.MORPH_CLOSE, se)
	assert(thres_img is not None)
	cv2.imshow("gg",thres_img)
	cv2.waitKey(0)
	config = '-l eng --oem 1 --psm 6'
	#s="samp.png"
	#cv2.imwrite(s,thres_img)
	
	#k=pytesseract.image_to_osd(Image.open('/home/dawnblade/darknet/samp.png'))
	#print(k)
	text = pytesseract.image_to_string(thres_img, config=config)
	val=[chr(x) for x in range (65,91)]
	val.extend([str(x) for x in range (0,10)])
	s1=''
	for i in text:
		if i in set(val):
			s1+=i
	 
	print('Result text: "{}"'.format(s1))


	
