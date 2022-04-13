# -*- coding: utf-8 -*-
"""
Tracking Graph
"""

## Imports
import matplotlib as mpl
import numpy as np
from sys import exit
from os import path
import seaborn as sns
import tkinter as tk
import matplotlib.pyplot as plt
import timeit

#%% Hardcoding

xDim = 192
yDim = 64
zDim = 48
threshold_value = 0.1

#%% Utility functions

def norm(x, y, z):
    return (x*x + y*y + z*z)**0.5    

#%% Loading Data
start = timeit.default_timer()

timesteps_min, timesteps_max = 70, 71 
        
data = [None]*(timesteps_max - timesteps_min)*xDim*yDim*zDim
dataU = [None]*(timesteps_max - timesteps_min)*xDim*yDim*zDim
dataV = [None]*(timesteps_max - timesteps_min)*xDim*yDim*zDim
dataW = [None]*(timesteps_max - timesteps_min)*xDim*yDim*zDim


folder_name = r"DataFiles"

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
                dataU[time_index*xDim*yDim*zDim + (k * yDim + j) * xDim + i] = (dataX[line_counter])
                dataV[time_index*xDim*yDim*zDim + (k * yDim + j) * xDim + i] = (dataY[line_counter])
                dataW[time_index*xDim*yDim*zDim + (k * yDim + j) * xDim + i] = (dataZ[line_counter])

                line_counter += 1

stop = timeit.default_timer()
print('\n Time taken to load ', timesteps_max-timesteps_min,'timesteps is :',stop - start,'seconds.')  
            
#%%2D Vector Field Plotting Function for a particular timestep

def plotting2DVectorField():
    plt.figure()
    timesteps_min, timesteps_max = 70, 71
    XsliceMin , XsliceMax = 0, 192
    YsliceMin, YsliceMax = 0, 64
    Zslice = 45
    skip = 5
    
    x,y = np.meshgrid(np.arange(-(XsliceMax-XsliceMin)/2,(XsliceMax-XsliceMin)/2,skip),np.arange(-(YsliceMax-YsliceMin)/2,(YsliceMax-YsliceMin)/2,skip))
    uVector = []
    vVector = []
    
    for i in range(XsliceMin, XsliceMax, skip):
        for j in range(YsliceMin, YsliceMax, skip):
            for time_index in range(0, (timesteps_max - timesteps_min)):
                u = dataU[time_index*xDim*yDim*zDim + (Zslice * yDim + j) * xDim + i] 
                v = dataV[time_index*xDim*yDim*zDim + (Zslice * yDim + j) * xDim + i] 
                uVector.append(u)
                vVector.append(v)
    plt.figure(0)
    plt.quiver(x, y, uVector, vVector, color='g', units='xy', scale=0.1)
    # x-lim and y-lim
    #plt.xlim(-2, 5)
    #plt.ylim(-2, 2.5)
    plt.title("2D Vector Field Plot")
    plt.grid()

    return

plotting2DVectorField()

#%%3D Vector Fiel

from mpl_toolkits.mplot3d import axes3d

def plotting3DVectorField():
    plt.figure()
    timesteps_min, timesteps_max = 70, 71
    XsliceMin, XsliceMax = 0, 192
    YsliceMin, YsliceMax = 0, 64
    ZsliceMin, ZsliceMax = 40, 45
    skip = 5
    
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    
    x, y, z = np.meshgrid(np.arange(-(XsliceMax-XsliceMin)/2,(XsliceMax-XsliceMin)/2,skip),
                          np.arange(-(YsliceMax-YsliceMin)/2,(YsliceMax-YsliceMin)/2,skip),
                          np.arange(-(ZsliceMax-ZsliceMin)/2,(ZsliceMax-ZsliceMin)/2,skip))
    
    uVector = []
    vVector = []
    wVector = []
    
    for i in range(XsliceMin, XsliceMax, skip):
        for j in range(YsliceMin, YsliceMax, skip):
            for k in range(ZsliceMin, ZsliceMax, skip):
                for time_index in range(0, (timesteps_max - timesteps_min)):
                    u = dataU[time_index*xDim*yDim*zDim + (k * yDim + j) * xDim + i] 
                    v = dataV[time_index*xDim*yDim*zDim + (k * yDim + j) * xDim + i]
                    w = dataW[time_index*xDim*yDim*zDim + (k * yDim + j) * xDim + i]
                    uVector.append(u)
                    vVector.append(v)
                    wVector.append(w)
    
    ax.quiver(x, y, z, uVector, vVector, wVector, length=0.05, color = 'black')
    
    
    return

plotting3DVectorField()