# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 16:21:34 2021

@author: madhu

@content: this file containt based code of taking user inputs and loading data
which is used to build the tracking_graph code
"""

#%%

## Imports
import matplotlib as mpl
import numpy as np
from sys import exit
from os import path

import matplotlib.pyplot as plt

#%% Hardcoding dataset description

xDim = 192
yDim = 64
zDim = 48

folder_name = r"DataFiles"

#%% User inputs for a selected area

xCount = 0
yCount = 0
zCount = 0

Zslice = int(input("Enter the Z Slice Value (1 to 48): "))
if (Zslice<1 or Zslice>48):
    exit()
    
XsliceMin = int(input ("Enter the X region starting range:(1 to 192) "))
XsliceMax = int(input ("Enter the X region ending range: (1 to 192) "))
if (XsliceMax<=XsliceMin):
    exit()
elif(XsliceMin<1 or XsliceMax>192):
    exit()

YsliceMin = int(input ("Enter the Y region starting range: (1 to 64) "))
YsliceMax = int(input ("Enter the Y region ending range: (1 to 64) "))
if (YsliceMax<=YsliceMin):
    exit()
elif(YsliceMin<1 or YsliceMax>64):
    exit()

#%% Utility functions

def norm(x, y, z):
    return (x*x + y*y + z*z)**0.5    

#%%

## Loading Data

timesteps_min, timesteps_max = 50, 55 # required timesteps
        
data = [None]*(timesteps_max - timesteps_min)*xDim*yDim*zDim #Empty array to load data

for time_index in range(0, (timesteps_max - timesteps_min)):
    timeperiod_filename = "flow_t"+str((time_index+timesteps_min)*4)+"8.data"
    
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


XsliceMin , XsliceMax = 155, 156 # Intrested x slice
YsliceMin, YsliceMax = 0, 64 # Intrested y slice
Zslice = 45 # Single slice of z

x_list = []
y_list = []

for i in range(XsliceMin, XsliceMax):
    for j in range(YsliceMin, YsliceMax):
        y_list = []
        for time_index in range(0, (timesteps_max - timesteps_min)):
            required_value = data[time_index*xDim*yDim*zDim + (Zslice * yDim + j) * xDim + i]
            y_list.append(required_value)
            plt.plot(y_list)
            
