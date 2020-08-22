# -*- coding: utf-8 -*-
"""
imageSegment.py

YOUR WORKING FUNCTION

"""
import cv2
import numpy as np

input_dir = 'input_sat/input'
output_dir = 'output/output'

# you are allowed to import other Python packages above
##########################
def segmentImage(img):
    # Inputs
    # img: Input image, a 3D numpy array of row*col*3 in BGR format
    #
    # Output
    # outImg: segmentation image
    #
    #########################################################################
    # ADD YOUR CODE BELOW THIS LINE

    # Convert image to Lab
    image_lab = cv2.cvtColor(img , cv2.COLOR_BGR2Lab)
      
    # split image to its respective channel
    l , a , b = cv2.split(image_lab)
    # perform otsu tresholding on to channel b of image
    
    ret , img_b = cv2.threshold(b  , 0 ,255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
    # check whether it fits 255 to 0 uint8

    # use ellipse kernel to obtain the curves when kernel performs operation 
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
    #perform morphological tuning    
    mask = cv2.morphologyEx(img_b, cv2.MORPH_CLOSE,kernel  )   
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN,kernel  )
    
    # create blank space to assign image that it not fully formed
    blank_mask = np.zeros(mask.shape, dtype=np.uint8)
    
    # perform contours operation on mask 
    cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # detect contours of x and y is 2 
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
    for c in cnts:
        cv2.drawContours(blank_mask,[c], -1, (255,255,255), -1)
        break
    
    
    outImg = blank_mask/255
    
    
    # END OF YOUR CODE
    #########################################################################
    return outImg
