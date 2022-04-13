# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 16:21:34 2021

@author: madhu

@content: 
"""

#%%

## Imports
import os
import cv2
import time
import scipy
import numpy as np
import matplotlib.pyplot as plt

from os import path
from PIL import Image
from scipy import ndimage
from matplotlib import patches
from matplotlib.image import imread

#%% Hardcoding dataset description

xDim = 192
yDim = 64
zDim = 48
timesteps_min, timesteps_max = 0, 102 # Required timesteps

folder_name = r"D:\Sync Drives\OneDrive - Indian Institute of Science\TWD\E0271_Project\Model_Files\DataFiles"

#%% Utility functions

def norm(x, y, z):
    return (x*x + y*y + z*z)**0.5    

def leading_zeros(num):
    return str(num).zfill(3)

def euclidean_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x2-x1)**2 + (y2 - y1)**2)**0.5
    
#%%

## Loading Data

timesteps_min, timesteps_max = 0, 102 # Required timesteps
        
data = [None]*(timesteps_max - timesteps_min)*xDim*yDim*zDim #Empty array to load data
for time_index in range(0, (timesteps_max - timesteps_min)):
    timeperiod_filename = "flow_t"+str((time_index + timesteps_min)*4).zfill(3)+"8.data"
    
    dataX = np.loadtxt(path.join(folder_name,timeperiod_filename), usecols=0,dtype='float')
    dataY = np.loadtxt(path.join(folder_name,timeperiod_filename), usecols=1,dtype='float')
    dataZ = np.loadtxt(path.join(folder_name,timeperiod_filename), usecols=2,dtype='float')

    line_counter = 0
    for k in range(0, zDim):
        for j in range(0, yDim):
            for i in range(0, xDim):
                data[time_index*xDim*yDim*zDim + (k * yDim + j) * xDim + i] = norm(dataX[line_counter], dataY[line_counter], dataZ[line_counter])
                line_counter += 1
                    
#%%

## Isocontours

XsliceMin , XsliceMax = 80, 192 # Intrested x slice
YsliceMin, YsliceMax = 10, 54 # Intrested y slice
Zslice = 24 # Single slice of z
isocontour_levels = 20

# Creating grid for iso contour function
x = np.linspace(XsliceMin, XsliceMax, (XsliceMax - XsliceMin))
y = np.linspace(YsliceMin, YsliceMax, (YsliceMax - YsliceMin))
X, Y = np.meshgrid(x, y)
Z = np.zeros(np.shape(X))

# Output images folder
output_images_folder = "OutputImages_smoke_levels_without_axis"
if not os.path.exists(output_images_folder):
    os.makedirs(output_images_folder)

plt.rcParams.update({'figure.max_open_warning': 0}) # suppress warnings

for time_index in range(0, (timesteps_max - timesteps_min)):
    for i in range(XsliceMin, XsliceMax):
        for j in range(YsliceMin, YsliceMax):
            Z[j - YsliceMin][i - XsliceMin] = data[time_index*xDim*yDim*zDim + (Zslice * yDim + j) * xDim + i]
    
    #time.sleep(1.5) # just so there consecutive graphs look like an animation
    
    # Plotting
    fig = plt.figure(time_index)
    plt.axis('off') # No need for axis while saving the image
    plt.contourf(X, Y, Z, isocontour_levels, cmap='Reds');
    #plt.contour(X, Y, Z, isocontour_levels, colors = 'black')
    #plt.imshow(Z, cmap = 'Greys')
    #file_name = 'f'+str(time_index)+'.png'
    #plt.savefig(path.join(output_images_folder, file_name), bbox_inches='tight', pad_inches = 0)
time.sleep(0.7)    
    
#%% 

## Vortex detection

input_images_folder = "D:\Sync Drives\OneDrive - Indian Institute of Science\TWD\E0271_Project\Results\Result Images\OutputImages_smoke_levels_without_axis_forCode"
output_images_folder = "Bounding_boxes"
if not os.path.exists(output_images_folder):
    os.makedirs(output_images_folder)

centroid_list_wrt_time = []
for time_index in range(0, (timesteps_max - timesteps_min)):
    file_name = "f"+str(time_index)+".png" # image file name
    img = np.array(Image.open(path.join(input_images_folder, file_name))) # load the image
    
    result = img.copy()
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert to grayscale image
    ret, thresh = cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY) # threshold the image
        
    # Draw contours with help of open cv
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    #contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #contours = contours[0] if len(contours) == 2 else contours[1]
    
    #fig, ax = plt.subplots(1)
    #plt.axis('off') # No need for axis 
    centroid_list = []
    for cntr in contours:
        x,y,w,h = cv2.boundingRect(cntr)
        centroid_list.append((x+(w/2), y+(h/2)))

        rect = patches.Rectangle((x,y),w,h, edgecolor='b', facecolor="none")
        #ax.imshow(result)
        #ax.add_patch(rect)
    
    centroid_list_wrt_time.append(centroid_list)
    
    # Plotting and saving image
    #plt.imshow(result, interpolation='nearest')
    #plt.imshow(thresh, cmap='gray') # to show the binary image with bouding box
    #file_name = 'f'+str(time_index)+'.png'
    #plt.savefig(path.join(output_images_folder, file_name), bbox_inches='tight', pad_inches = 0)
    
   

#%% 

## Tracking Graph in 3D
%matplotlib auto 

fig = plt.figure(figsize = (10, 7))
#fig = plt.figure(figsize = (10, 7))
ax = plt.axes(projection ="3d")

start_index, end_index = 30, 60
t_minus_1_ponits = centroid_list_wrt_time[start_index]

for time_index in range(start_index + 1, end_index):
    for point in centroid_list_wrt_time[time_index]:
                
        minimum = 1000
        min_index = -1
        for past_point_index in range(0, len(t_minus_1_ponits)):
            past_point = t_minus_1_ponits[past_point_index]
            dist = euclidean_distance(point, past_point) 
            if dist < minimum:
                minimum = dist
                min_index = past_point_index
        if minimum > 70:
            continue # point is born
        required_past_point = t_minus_1_ponits[min_index]
   
        x = np.array([required_past_point[0], point[0]])
        y = np.array([required_past_point[1], point[1]])
        z = np.array([time_index - 1, time_index])
        ax.plot(x, z, y, color = "green")
        #break
    t_minus_1_ponits = centroid_list_wrt_time[time_index]
    
# Creating figure

# Creating plot

ax.set_xlabel('X-axis', fontweight ='bold')
ax.set_ylabel('Time-axis', fontweight ='bold')
ax.set_zlabel('Y-axis', fontweight ='bold')
plt.title("Tracking Graph in 3D")

# show plot
plt.show()

#%% Trail codes

plt.figure(3000)
for LineCollection in return_object.collections:
    fig, ax = plt.subplots()
    ax.add_artist(LineCollection)
    break

#print(np.shape(img))
#threshold = 200
#binary_mask = img > threshold
#selection = np.zeros_like(img)
#selection[binary_mask] = img[binary_mask]