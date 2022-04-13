# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 15:18:12 2021

@author: madhu
"""

import cv2
import os

image_folder = r'Bounding_boxes'
video_name = r'Bounding_boxes.avi'

images = []
for time_index in range(0,102):
    file_name = 'f'+str(time_index)+'.png'
    images.append(file_name)
 
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 5, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()