# Vortex-Shedding-Visualization

## Visualization of Vortex Shedding in 3D Flow Around a Confined Square Cylinder using Tracking Graphs    

Note: This is a Project work done as a part of E0 271 - Graphics and Visualization course work in Indian Institute of Science (IISc), Bangalore during Aug - Dec 2021.

**Team Members:**  
1. Sankar. B - PhD, Mechanical  
2. Masavir Khliq - M.Tech CSA  
3. Phani Madhusudan Thontepu - M.Tech AI

### 1. Problem Statement  
Exploring and analyzing the spatio-temporal evolution of features in largescale timevarying
datasets is a common problem in many areas of science and engineering. One such
area pertaining to this problem is the Fluid Mechanics and Combustion Dynamics where
the flow of Newtonian fluids particularly gases have the propensity to demonstrate chaotic
unsteady turbulent behavior. Advanced Simulations can predict the behavior of the fluids
in situations that are prone to be difficult when conducted as experiments and measuring
different data using sensors. A simple fluid flow animation requires solving complex PDE
of Navier-Stokes Equation. Advanced solvers with parallel computing systems are even
able to solve the DNS of Navier-Stokes equation subjected to certain boundary conditions
and assumptions. But the main outcome of doing this lies not only in just solving these
equations but understanding the resulting data of Velocity and Pressure. The problem
with that is simulations generate mountains of data which makes it difficult and even
impossible for the human mind to process them. Hence better visualization strategies
are needed to understand the data and the spatio-temporal feature attributes. Hence we
aim to develop a strategy that helps in a streamlined understanding of large dataset and
able to track certain physical phenomenon of interest like the Vortex Shedding behavior
in the Fluid flow around a Bluff body.  

### 2. Objective  
• To Develop Visualizations that demonstrates the Spatial-Time Evolving Features in
3D Flow around a Confined Cylinder dataset using the concept of Tracking Graph  
• To able to track the transition from Laminar to Turbulent flow regime in the different
timesteps  
• To figure out the important subset region of interest out of the entire set of 4D
volume of data 192x64x48x102  
• To understand the behaviour of Vortex Shedding Phenomenon (Von Kármán Vortex
Street) by tracking each and every vortex separately  
• To understand how different Visualization techniques perform under the increasing
unsteadiness of the fluid flow  
• To demonstrate the Streamlines, Streaklines and Pathlines in a 3D Visualization  

### 3. Tasks Accomplished  
**• Exploring Dataset – 3D Flow around a confined Square Cylinder:**  
This was done to read the Amira mesh format and convert to data files and then
covert to VTK file format. Here we used C++ and Amira mesh to accomplish this
task.  
**• Contour Plot for all the 102 timesteps with span of 192 x 64 for a mid plane Z
slice = 24:**  
This was done to identify the various feature regions in the dataset including vortex
and visualize the Von Karman Street Phenomenon. Here we used python and
matplotlib to accomplish this task.  
**• Image Processing of all the Contour Plots:**  
This was done to identify and track the movement of each and every vortex separately.
Here we used python and OpenCV to accomplish this task.  
**• Tracking Graph in 3D:**  
This was done to plot the birth and death of vortex and visualize the Vortex Shedding.
To do this task we used Python and Matplotlib.  
**• Vector Field Plot:**  
We did this to deduce the region of interest to focus more on to identify the behaviour
of one vortex. This task was also done by python and Matplotlib.  
**• Tracking Graph in 2D:**  
To identify the critical timestep and region of interest and the pattern of repetitive
behaviour of the Vortex tracking graph is 2d was plotted. Python and Matplotlib
was used to do this task.  
**• VTK File Dataset:**  
This was done to convert the data files created earlier into VTK file format –
Structured Points + Vector Field. C++ was used to accomplish this task.  
**• 3D Visualization of Vector Field and Streamlines:**  
By this task we Visualized the Behaviour of Laminar and Turbulent flow behaviour
at a particular timestep. Tools used here were VTK, Paraview.  

### 4. Conclusion  
• Explored the dataset.  
• Understood the formation and dissipation of Vortices and the phenomenon of Vortex
Shedding (Von Karman Vortex Street)  
• Visualized the Vector field flow around a bluff body.  
• Able to distinguish the flow regimes from laminar to turbulent and the transition
regions.  
• Implement our approach on the OpenCV based Tracking Graph Plotting in 3D
using Vortex Detection in contour plots.  
• Understood the importance of optimization layout in the Feature Tracking graph
in 2D.  
• Found the critical regions downstream behind the square cylinder block where the
flow becomes unsteady.  

### 5. Scope for Improvement    
• There are lots of intersections in the tracking graph in 2D even after limiting the
region of interest, hence in order to minimize intersections optimization of the layout
has to be carried out  
• There is no connectivity between different visualizations and there is no interactive
exploration in the visualization which can be added  

### 6. Responsibilities of Each Member   
All three of us worked as a team. We read the related material individually and then
discussed it together. In this way we got better understanding of what we were doing.  
• Sankar coming from a Mechanical background was able to understand the Fluid
Mechanics flow concepts better and explained to Phani and Masavir. Masavir being
Computer Science Student was able to explain the algorithmic implementation
in the paper “Interactive Exploration of Large Scale time varying datasets using
Dynamic Tracking Graphs”. Phani being an AI person was able to explain the importance
of large dataset and the ways to handle them effectively. This enhanced
our overall understanding.  
• Phani implemented the first two tasks on drawing the contour plots and using Image
processing to identify the vortices. Phani also wrote the script to convert the Amira
mesh file to the data files. Sankar was able to draw the Tracking Graphs and do
the Vector field plots using Python. Masavir wrote the script to convert the data
files to VTK files. He then used paraview to visualize the data in 3D.  
• Finally each one of us contributed to other’s work by providing constructive comments
on improvements and scrutinizing the work in such a way that the overall
outcome what we have presented above were able to be achieved successfully.  

### 7. References  
1. Wathsala Widanagamaachchi, Cameron Christensen, Peer-Timo Bremer, Valerio
Pascucci: Interactive exploration of large-scale time-varying data using dynamic
tracking graphs. LDAV 2012: 9-17  
2. Background: https://www.csc.kth.se/ weinkauf/notes/squarecylinder.html  
3. Dataset (102-time steps, velocity): https://www.csc.kth.se/ weinkauf/notes/squarecylinder.html  
4. F. Reinders, F. H. Post, H. J. W. Spoelder, “Visualization of time-dependent data
using feature tracking and event detection”. The Visual Computer, 17:55-71, 200l.  
5. R. Samtaney, D. Silver, N. Zabusky, and J. Cao. Visualizing features and tracking
their evolution. Computer, 27(7):20-27, July 1994.  
6. Topological structural analysis of digitized binary images by border following - https://www.sciencedirect.com/science/article/pii/0734189X85900167  
7. Quadtree Algorithms for Contouring Functions of Two Variables - https://academic.oup.com/comjnl/article-pdf/33/5/402/1299079/330402.pdf   
8. Plotting Vector Feilds - https://krajit.github.io/sympy/vectorFields/vectorFields.html  
9. Contour Detection using OpenCV - https://learnopencv.com/contour-detection-using-opencv-python-c/   
10. Three-Dimensional Plotting in Matplotlib - https://jakevdp.github.io/PythonDataScienceHandbook/04.t12-three-dimensional-plotting.html   

