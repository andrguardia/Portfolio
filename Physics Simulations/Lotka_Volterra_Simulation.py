# -*- coding: utf-8 -*-
"""Lotka-Volterra.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/WereszczynskiClasses/assignment-week-9-andrguardia/blob/main/Lotka_Volterra.ipynb

#The Lotka-Volterra equations

The Lotka-Volterra equations are a mathematical model of predator-prey interactions between biological species.  Let two variables $x$ and $y$ be proportional to the size of the populations of two species, traditionally called "rabbits" (the prey) and "foxes" (the predators).  You could think of $x$ and $y$ as being the population in thousands, say, so that $x=2$ means there are 2000 rabbits.  Strictly the only allowed values of $x$ and $y$ would then be multiples of 0.001, since you can only have whole numbers of rabbits or
foxes.  But 0.001 is a pretty close spacing of values, so it's a decent
approximation to treat $x$ and $y$ as continuous real numbers so long as
neither gets very close to zero.

In the Lotka-Volterra model the rabbits reproduce at a rate proportional
to their population, but are eaten by the foxes at a rate proportional to
both their own population and the population of foxes:

$
\frac{dx}{dt} =  \alpha x - \beta xy$

where $\alpha$ and $\beta$ are constants.  At the same time the foxes
reproduce at a rate proportional the rate at which they eat
rabbits-because they need food to grow and reproduce-but also die of
old age at a rate proportional to their own population:

$
\frac{dy}{dt} = \gamma xy - \delta y
$

where $\gamma$ and $\delta$ are also constants.

##A. 

Write a program to solve these equations using the fourth-order
  Runge-Kutta method for the case $\alpha=1$, $\beta=\gamma=0.5$, and
  $\delta=2$, starting from the initial condition $x=y=2$.  Have the
  program make a graph showing both $x$ and $y$ as a function of time on
  the same axes from $t=0$ to $t=30$.  (Hint: Notice that the differential
  equations in this case do not depend explicitly on time $t$ in vector
  notation, the right-hand side of each equation is a function $f(\vec{r})$
  with no $t$ dependence.  You may nonetheless find it convenient to define
  a Python function ```f(r,t)``` including the time variable, so that your
  program takes the same form as other programs we've written.
  You don't have to do it that way, but it can avoid some confusion.)
"""

import numpy as np
import matplotlib.pyplot as plt
#Setting Initial Conditions
start =  0.0 #Start Time
end   = 30.0 #End Time
r_0   =  np.array([2.0,2.0]) #Initial Value Array
t_0   =  0.0 #Initial Time Value
#Define Constants
alpha = 1
beta = 0.5
gamma = 0.5
delta = 2
h  =  0.001
#Define Three Dimensional Function
def f(r,t):
  x = r[0] #Initialize x
  y = r[1] #Initialize y
  fx = alpha*x-beta*x*y #dx/dt
  fy = gamma*x*y-delta*y #dy/dt
  return np.array([fx,fy]) #Return Derivative Array

#Applying 4th Order Runge Kutta Method
N = int((end-start)/h) +1 #Define Slice Number
rp = np.zeros((N,2)) #Initialize r values Matrix of Nx2 dimensions
tp = np.zeros(N) #Initialize time array of length N
rp[0] = r_0 #Initialize r
tp[0] = t_0 #Initialize t
for n in range(N-1): #Calculate RK Integral
  tp[n+1] = h * (n+1)
  r = rp[n]
  t = tp[n]
  k_1 = h*f(r,t)
  k_2 = h*f(r+ 0.5 *k_1,t+0.5*h)
  k_3 = h*f(r+ 0.5 *k_2,t+0.5*h)
  k_4 = h*f(r+ k_3, t+h)
  rp[n+1] = r + (k_1+2*k_2+2*k_3+k_4)/6
#Plot Rabbit and Fox Population vs Time
plt.plot(tp,rp[:,0],label='Rabbit Population')
plt.plot(tp,rp[:,1],label='Fox Population')
plt.xlabel('Time (s)')
plt.ylabel('Population (In Thousands)')
plt.title('Population vs Time')
plt.legend()
plt.show()

"""##B.

Describe in words what is going on in the system, in terms of rabbits
  and foxes.

> As stated above, the populations of rabbits and foxes are interconnected by the fact that as the rabbit population grows, foxes are able eat more and thus reproduce, which results in their population growing. As the fox population grows, foxes eat more rabbits, which results in the rabbit population decreasing. This causes the immediate decrease of the fox population due to a food shortage. This decrease in fox population results in a surge in rabbit population, since they are not being eaten, and the cycle starts again.


> This is the precise behavior that can be observed in the graph above, the rabbit population increases, the fox population starts growing with a certain delay. After the fo population reaches a critical value, the rabbit populating decreases significantly, which in term causes the decrease in the fox population. These two population numbers constantly oscillate as the graph above shows.
"""