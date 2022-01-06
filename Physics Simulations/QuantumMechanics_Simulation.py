# -*- coding: utf-8 -*-
"""PHYS301_Final_Paper.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uye682KCf23KqhD_a55a8geXmTC-ypeb

#Simulation Main
The figure below shows the different energy levels for an electron, muon and tau particles bounded within a rectangle of width 1nm and length 2nm with Möbius Strip boundary conditions.
"""

import numpy as np
#Constants:

hbar = 6.5821e-16 # eV*s
pi = 3.1416

#Möbius Strip Dimensions: 

L = 2e-9 # meters
W = 1e-9 # meters

#Particle Masses: 

m_electron = (0.510998946e6)*(8.98755179e16)  #eV*s^2/m^2
m_muon = (105.7e6)*(8.98755179e16) #eV*s^2/m^2
m_tau = (1776.8e6)*(8.98755179e16) #eV*s^2/m^2

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np

def eigenval_plot(mass,nxmax,nymax,L,W,title): 
  fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
  # Make data.
  n_x = np.arange(0, nxmax,1)
  n_y = np.arange(0, nymax,1)
  X = n_x
  Y = n_y
  X, Y = np.meshgrid(X, Y)
  C = ((hbar**2)*(pi**2)/(2*mass)) #Put all these constant terms into a constant to simplify code
  E = np.zeros((nxmax,nymax))
  for i in n_x:
    for j in n_y:
      E[i,j]= C*(((2*n_x[i]+1)/L)**2 + ((2*n_y[j])/W)**2)
    j=j+1
    i=i+1
  Z = E
  # Plot the surface.
  surf = ax.plot_surface(X, Y, Z, cmap='viridis', linewidth=1, antialiased=True)
  #Customize axis labels
  ax.set_xlabel('n_x')
  ax.set_ylabel('n_y')
  ax.set_zlabel('Energy   ')
  plt.title(title)
  # Customize the z axis.
  ax.zaxis.set_major_locator(LinearLocator(10))
  # Add a color bar which maps values to colors.
  fig.colorbar(surf, shrink=0.6, aspect=20)
  ax.view_init(25, 140)
  ax.dist = 11.5
  fig
  plt.show()

eigenval_plot(m_electron,10,10,2e-9,1e-9,"Energy Eigenvalues: Electron Mass")

eigenval_plot(m_muon,10,10,2e-9,1e-9,"Energy Eigenvalues: Muon Mass")

eigenval_plot(m_tau,10,10,2e-9,1e-9,"Energy Eigenvalues: Tau Mass")

eigenval_plot(m_electron,100,100,2e-9,1e-9,"Energy Eigenvalues nx=100 and ny=100")

eigenval_plot(m_electron,10,10,100e-9,1e-9,"Energy Eigenvalues: L = 100nm")

eigenval_plot(m_electron,10,10,1e-9,100e-9,"Energy Eigenvalues: W = 100nm")

"""#Figure 1: Mobius Strip"""

def mobius(n,title):
  from mpl_toolkits import mplot3d
  import numpy as np
  import matplotlib.pyplot as plt
  theta = np.linspace(0, 2 * np.pi, 50)
  w = np.linspace(-0.3, 0.3, 100)
  w, theta = np.meshgrid(w, theta)
  phi =  theta*n/2
  # radius in x-y plane
  r = 1 + w * np.cos(phi)
  x = np.ravel(r * np.cos(theta))
  y = np.ravel(r * np.sin(theta))
  z = np.ravel(w * np.sin(phi))
  from matplotlib.tri import Triangulation
  tri = Triangulation(np.ravel(w), np.ravel(theta))
  ax.plot_trisurf(x, y, z, triangles=tri.triangles,
                cmap='viridis', linewidths=1);
  ax.set_xlim(-1, 1); ax.set_ylim(-1, 1); ax.set_zlim(-1, 1); 
  ax.dist = 11.5
  plt.title(title)
  ax.zaxis.set_major_locator(LinearLocator(5))
  ax.xaxis.set_major_locator(LinearLocator(5))
  ax.yaxis.set_major_locator(LinearLocator(5))

import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from mpl_toolkits.mplot3d.axes3d import get_test_data


# set up a figure twice as wide as it is tall
fig = plt.figure(figsize=plt.figaspect(1/4))
ax = fig.add_subplot(1, 3, 1, projection='3d')
mobius(1,'Mobius Strip with n = 1 Half Turns')
ax = fig.add_subplot(1, 3, 2, projection='3d')
mobius(3,'Mobius Strip with n = 3 Half Turns')
ax = fig.add_subplot(1, 3, 3, projection='3d')
mobius(5,'Mobius Strip with n = 5 Half Turns')
plt.show()

"""#Figure 2: Mass Variation Effect on Energy Eigenvalues"""

def eigenval_plot(mass,nxmax,nymax,L,W,title): 
  #fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
  # Make data.
  n_x = np.arange(0, nxmax,1)
  n_y = np.arange(0, nymax,1)
  X = n_x
  Y = n_y
  X, Y = np.meshgrid(X, Y)
  C = ((hbar**2)*(pi**2)/(2*mass)) #Put all these constant terms into a constant to simplify code
  E = np.zeros((nxmax,nymax))
  for i in n_x:
    for j in n_y:
      E[i,j]= C*(((2*n_x[i]+1)/L)**2 + ((2*n_y[j])/W)**2)
    j=j+1
    i=i+1
  Z = E
  # Plot the surface.
  surf = ax.plot_surface(X, Y, Z, cmap='viridis', linewidth=1, antialiased=True)
  #Customize axis labels
  ax.set_xlabel('n_x')
  ax.set_ylabel('n_y')
  ax.set_zlabel('Energy   ')
  plt.title(title)
  # Customize the z axis.
  ax.zaxis.set_major_locator(LinearLocator(5))
  # Add a color bar which maps values to colors.
  ax.view_init(25, 140)
  ax.dist = 10
  fig

import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from mpl_toolkits.mplot3d.axes3d import get_test_data

# set up a figure twice as wide as it is tall
fig = plt.figure(figsize=plt.figaspect(0.3))
ax = fig.add_subplot(1, 3, 1, projection='3d')
eigenval_plot(m_electron,10,10,2e-9,1e-9,'Energy Eigenvalues: Electron Mass')
ax = fig.add_subplot(1, 3, 2, projection='3d')
eigenval_plot(m_muon,10,10,2e-9,1e-9,'Energy Eigenvalues: Muon Mass')
ax = fig.add_subplot(1, 3, 3, projection='3d')
eigenval_plot(m_tau,10,10,2e-9,1e-9,'Energy Eigenvalues: Tau Mass')
plt.show()

# set up a figure twice as wide as it is tall
fig = plt.figure(figsize=plt.figaspect(0.3))
ax = fig.add_subplot(1, 3, 1, projection='3d')
eigenval_plot(m_electron,10,10,2e-9,1e-9,"Energy Eigenvalues nx=10 and ny=10")
ax = fig.add_subplot(1, 3, 2, projection='3d')
eigenval_plot(m_electron,100,100,2e-9,1e-9,"Energy Eigenvalues nx=100 and ny=100")
ax = fig.add_subplot(1, 3, 3, projection='3d')
eigenval_plot(m_electron,1000,1000,2e-9,1e-9,"Energy Eigenvalues nx=1000 and ny=1000")
plt.show()