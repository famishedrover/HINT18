import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from matplotlib import pyplot as plt 
from keras.layers import Conv2D, MaxPooling2D, Convolution2D, Dropout, Dense, Flatten, LSTM
from keras.models import Sequential, save_model
from keras.models import model_from_yaml
from keras.utils import np_utils
from scipy.io import loadmat
import pickle
import argparse
import keras
import numpy as np
import cv2

mapping = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z', 26: 'B_', 27: 'D_', 28: 'J_', 29: 'P_'}
# mapping = {0: 48, 1: 49, 2: 50, 3: 51, 4: 52, 5: 53, 6: 54, 7: 55, 8: 56, 9: 57, 10: 65, 11: 66, 12: 67, 13: 68, 14: 69, 15: 70, 16: 71, 17: 72, 18: 73, 19: 74, 20: 75, 21: 76, 22: 77, 23: 78, 24: 79, 25: 80, 26: 81, 27: 82, 28: 83, 29: 84, 30: 85, 31: 86, 32: 87, 33: 88, 34: 89, 35: 90, 36: 97, 37: 98, 38: 99, 39: 100, 40: 101, 41: 102, 42: 103, 43: 104, 44: 105, 45: 106, 46: 107, 47: 108, 48: 109, 49: 110, 50: 111, 51: 112, 52: 113, 53: 114, 54: 115, 55: 116, 56: 117, 57: 118, 58: 119, 59: 120, 60: 121, 61: 122}

#  IMPORTANT STEP 
yaml_file = open('model.yaml', 'r')
loaded_model_yaml = yaml_file.read()
yaml_file.close()
print("Read Model Architecture.")
model = model_from_yaml(loaded_model_yaml)
weights= "wt_0.h5"
weights_old = "model_old.h5"
model.load_weights(weights)
print("Loaded Model Weights.")
model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])



# image in numpy
def actualData(image , original_char):
	# print image[0][0]
	# if image[0][0] > 150 :
	# 	image = 255-image
	# else :
	# 	pass

	image = 255 - image
	actualTest = cv2.resize(image , (28,28),interpolation = cv2.INTER_AREA)
	_,actualTest = cv2.threshold(actualTest,10,255,cv2.THRESH_BINARY)
	# actualTest = cv2.resize(image , (28,28),interpolation = cv2.INTER_LINEAR)
	# actualTest = cv2.resize(image , (28,28),interpolation = cv2.INTER_NEAREST)
	# plt.imshow(actualTest,cmap='gray_r')
	# plt.show()
	
	ans = model.predict_proba(actualTest.reshape(1,28,28,1),verbose=0)
	ochar = 1
	print (ans)
	for k,v in mapping.iteritems():
		if v==original_char:
			# print 'Matched:',original_char,' at pos ',k
			ochar = k
	# print ans 
	# print ochar
	orig_prob = ans[0][ochar]
	max_prob = ans[0][ans.argmax()]
	max_char = mapping[ans.argmax()]
	return (orig_prob , max_prob , max_char)


if __name__ == '__main__':
	actualTest = cv2.imread('actualTest/D_2.png',0)
	# plt.imshow(actualTest,cmap='gray_r')
	# plt.show()
	op , mp , mc = actualData(actualTest,'D_')
	print (op , mp , mc )

	actualTest = cv2.imread('actualTest/D_1.png',0)
	# plt.imshow(actualTest,cmap='gray_r')
	# plt.show()
	op , mp , mc = actualData(actualTest,'D_')
	print (op , mp , mc )

	actualTest = cv2.imread('actualTest/D1.png',0)
	# plt.imshow(actualTest,cmap='gray_r')
	# plt.show()
	op , mp , mc = actualData(actualTest,'D')
	print (op , mp , mc )
