# -*- coding: utf-8 -*-
"""
Tracking Graph
"""

#%% Imports
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

#%% User inputs

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

#%% Loading Data
start = timeit.default_timer()

timesteps_min, timesteps_max = 50, 80
        
data = [None]*(timesteps_max - timesteps_min)*xDim*yDim*zDim
dataU = [None]*(timesteps_max - timesteps_min)*xDim*yDim*zDim
dataV = [None]*(timesteps_max - timesteps_min)*xDim*yDim*zDim
dataW = [None]*(timesteps_max - timesteps_min)*xDim*yDim*zDim


folder_name = r"D:\Sync Drives\OneDrive - Indian Institute of Science\TWD\E0271_Project\Model_Files\DataFiles"

for time_index in range(0, (timesteps_max-timesteps_min)):
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

#%% Plotting Function

threshold_value = 0.3

def plotting(input_data,th_value,title):
    timesteps_minIndex, timesteps_maxIndex = 0, 30
    XsliceMin , XsliceMax = 60, 80
    YsliceMin, YsliceMax = 30, 40
    Zslice = 20
    threshold_value = th_value
    
    
    sca_time_list_pervertex = []
    timestep_data = []
    
    for i in range(XsliceMin, XsliceMax):
        for j in range(YsliceMin, YsliceMax):
            sca_time_list_pervertex = []
            timestep_data = []
            for time_indexp in range(timesteps_minIndex, timesteps_maxIndex):
                data = input_data
                required_value = data[time_indexp*xDim*yDim*zDim + (Zslice * yDim + j) * xDim + i]
                if (time_indexp==timesteps_minIndex):
                    previous_value = required_value
                else:
                    previous_value = data[(time_indexp-1)*xDim*yDim*zDim + (Zslice * yDim + j) * xDim + i]
                if(abs(required_value-previous_value)<=threshold_value):
                    None
                else:
                    sca_time_list_pervertex.append(required_value)
                    timestep_data.append(time_indexp)
                with sns.color_palette("Spectral", n_colors=50):
                    plt.plot(timestep_data,sca_time_list_pervertex)
                    plt.title(title)
                    plt.xlabel("Timesteps Data")
                    plt.ylabel("Flow Field Data")
    
    return

plotting(data,threshold_value,'Tracking Graph (Magnitude)')

#%% Tracking Graph Plotting for Magnitude, U, V, W separately
plotting(data,threshold_value,'Tracking Graph (Magnitude)')
plotting(dataU,threshold_value,'Tracking Graph (u in x direction)')
plotting(dataV,threshold_value,'Tracking Graph (v in y direction)')
plotting(dataW,threshold_value,'Tracking Graph (w in z direction)')

#%% GUI
# import all classes/methods
# from the tkinter module
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

# The main tkinter window
window = Tk()
  
# setting the title and 
window.title('Tracking Graph Application')
  
# setting the dimensions of the main window
window.geometry("500x400")

#setting icon
#window.iconbitmap('')

def plot_tg():
   # plotting the graph
   plotting(data,threshold_value,'Tracking Graph (Magnitude)')
   plotting(dataU,threshold_value,'Tracking Graph (u in x direction)')
   plotting(dataV,threshold_value,'Tracking Graph (v in y direction)')
   plotting(dataW,threshold_value,'Tracking Graph (w in z direction)')

# button that would displays the plot
plot_button = Button(master = window, command = plot_tg, height = 4, width = 20, text = "Plot")
plot_button.pack(side=RIGHT, padx=150, pady=150)

# place the button into the window
plot_button.pack()
  
# run the gui
window.mainloop()