import cv2
import numpy as np
#import image
# import sys
# sys.path.append('../')
# from charpred import actualData
from runcheck import actualData
# from matplotlib import pyplot as plt

def ocr_word(ans_list):
	f = ''
	for ix in ans_list:
		f+= str(ix[-1])
	return f


def segment_word(image , word):

	gray = image
	try :
		gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	except :
		pass
	# #binary
	ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
	# #dilation
	kernel = np.ones((5,5), np.uint8)
	img_dilation = cv2.dilate(thresh, kernel, iterations=1)
	kernel = np.ones((7,1), np.uint8)
	img_dilation = cv2.dilate(img_dilation, kernel, iterations=9)
	#find contours
	_,ctrs, hier = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	#sort contours
	sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])

	ans_list = []
	for i, ctr in enumerate(sorted_ctrs):
	    # Get bounding box
	    x, y, w, h = cv2.boundingRect(ctr)
	    # print w,h
	    # print cv2.contourArea(ctr)
	    # print '-'*20

	    # Getting ROI
	    roi = image[y:y+h, x:x+w]


	    t,b,l,r = 0,0,0,0
	    if h>w:
	    	l = r = (h-w)/2
	    elif w>h :
	    	t = b = (w-h)/2
	    else :
	    	t =b =l = r = 0

	    constant_roi= cv2.copyMakeBorder(roi,t,b,l,r,cv2.BORDER_CONSTANT,value=[255,255,255])
	    constant_roi = cv2.cvtColor(constant_roi, cv2.COLOR_BGR2GRAY)
	    # constant_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
	    print 'Constant ROI shape in function segment_word :',constant_roi.shape
	    # ----------------------------------- PROCESS ROI HERE -----------------------------------

	    ans_list.append(actualData(constant_roi,word[i]))

	    # ----------------------------------- TILL HERE ------------------------------------------
	    # show ROI
	    # plt.imshow(constant_roi,cmap='gray_r')
	    # plt.show()
	    # cv2.imshow('segment no:'+str(i),constant_roi)
	    # cv2.rectangle(image,(x,y),( x + w, y + h ),(90,0,255),2)
	    # cv2.waitKey(0)
	return ans_list


if __name__ == '__main__':
	# from matplotlib import pyplot as plt
	image = cv2.imread('actualTest/test5.png')
	ans = segment_word(image,'MATH')
	print ocr_word(ans)
	# plt.imshow(image)
	# plt.show()
	# cv2.imshow('marked areas',image)
	# cv2.waitKey(0)