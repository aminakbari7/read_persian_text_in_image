import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import cv2
import numpy as np
import re
import arabic_reshaper
from bidi.algorithm import get_display
im=cv2.imread('image.jpg')
scale_percent = 180 
width = int(im.shape[1] * scale_percent / 100)
height = int(im.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(im, dim, interpolation = cv2.INTER_AREA)
gray_image = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
enhanced_image = cv2.addWeighted(gray_image, 0.5, gray_image, 0, 30)
original_and_enhanced_image = np.hstack((gray_image, enhanced_image))
reshaped_text = arabic_reshaper.reshape(pytesseract.image_to_string(enhanced_image,lang='fas' ))
reshaped_text = arabic_reshaper.reshape(reshaped_text)
bidi_text = get_display(reshaped_text)
print(bidi_text)
cv2.imshow('result',enhanced_image)
cv2.waitKey(0)