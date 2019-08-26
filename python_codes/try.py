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

import cv2
import pytesseract
import os
from PIL import Image
import numpy as np
import sys

from scipy.ndimage import interpolation as inter


img1=cv2.imread("/home/dawnblade/darknet/"+sys.argv[1])
c=0
for i in co_od:
	#315, 307, 425, 261
	crop_img=img1[i[3]:i[1],i[0]:i[2]].copy()
	cv2.imwrite("plates/plate{}.png".format(c), crop_img)
	c+=1
#cv2.waitKey(0)
