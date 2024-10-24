import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from __future__ import division
from sympy import *
from sympy.solvers.solveset import linsolve
import math


#Task 1

x, y, b_w, b_f, h, E, L, p, k, p_min, p_max = symbols('x y b_w b_f h E L p k p_min p_max')
C1,C2,C3,C4 = symbols('C1 C2 C3 C4')

u = Function('u')

b = (4*(b_f-b_w)*y**2)/(h**2)+b_w #b(y)- shape of parabola 
A = integrate(2*b, (y,0,h/2)) # Area
Q = integrate(b*y, (y,y,h/2)) # The first moment of inertia
I = integrate(2*b*y**2, (y,0,h/2)) # The second moment of inertia
print (A,'= A(y)')
print (Q,'= Q(y)')
print (I,'= I(y)')

#Task 2

p=(4*(p_min-p_max)*x**2)/(L**2)-(4*(p_min-p_max)*x)/(L)+p_min #shape of p(x)
ODE = E*I*Derivative(u(x),x,x,x,x) - p #ODE for our case 

print ("0 = ")
display(ODE)

#Task 3

u=dsolve(ODE,u(x)).rhs # solve the ODE

print('u=')
display(u)

du    = u.diff(x) #the first derivative of displacement 
ddu   = u.diff(x,x) #the second derivative of displacement 
dddu  = u.diff(x,x,x) #the third derivative of displacement 

#Task 4

#For simply supported beam
bc1 = u.subs(x,0) #displacement (x=0)=0, fix end
bc2 = du.subs(x,0) # slope (x=0)=0, fix end
bc3 = u.subs(x,L) #displacement (x=L)=0, fix end
bc4 = du.subs(x,L) # slope (x=L)=0, fix end


#Task 5

sol=linsolve([bc1, bc2, bc3, bc4], (C1,C2,C3,C4)) #substitute bc in equation 
[C1sol,C2sol,C3sol,C4sol] = list(sol)[0] # input constants in 1 list 
usol= u.subs([(C1,C1sol), (C2,C2sol), (C3,C3sol), (C4,C4sol)]) #substitute C1, C2, C3, C4 in equation
print('u(x)=')
display(usol)

#Task 6

MSol   = E*I*diff(usol,x,x)   # Moment
VSol   = E*I*diff(usol,x,x,x) # Shear

sigmaxxSol =abs((MSol * y) / I) # sigmaxx
sigmaxySol =(VSol*Q)/(b*I) # sigmaxy
sigmavmSol =  ((sigmaxxSol**2)+3*(sigmaxySol**2)) # Von Mises stress


print ("M(x) = ")
display(MSol)

print ("V(x) = ")
display(VSol)

print ("sigma_xx = ")
display(sigmaxxSol)

print ("sigma_xy = ")
display(sigmaxySol)

print ("sigmavm = ")
display(sigmavmSol)


#Task 7

valE      = 200e9  # Pa
valL      = 15     # m
valb_f    = 0.25   # m
valp_max      = -20000 # N/m
valp_min      = 0 # N/m
valro         = 7800 #kg/m**3

u_lim     = valL/250
sigma_y   = 180e6 # Pa

h_min     = 0.01 #m
h_max     = 0.5 #m

b_min     = 0.01 #m
b_max     = valb_f #m

uSub       = usol.subs  ([(E,valE),(L,valL),(x,valL/2),(p_max,valp_max),(p_min,valp_min),(b_f,valb_f)])

ASub       = A.subs       ([(b_f,valb_f)])

sigmavmSub1 = sigmavmSol.subs ([(E,valE),(L,valL),(x,0), (y,h/2),(p_max,valp_max),(p_min,valp_min),(b_f,valb_f)]) #stress at point (0,h/2)
sigmavmSub2 = sigmavmSol.subs ([(E,valE),(L,valL),(x,valL/2), (y,-h/2),(p_max,valp_max),(p_min,valp_min),(b_f,valb_f)]) #stress at point (L/2, -h/2)
sigmavmSub3 = sigmavmSol.subs ([(E,valE),(L,valL),(x,0), (y,0),(p_max,valp_max),(p_min,valp_min),(b_f,valb_f)]) #stress at point (0, 0)
sigmavmSub4 = sigmavmSol.subs ([(E,valE),(L,valL),(x,valL/4), (y,h/4),(p_max,valp_max),(p_min,valp_min),(b_f,valb_f)]) #stress at point (L/4, h/4)

print('u=')
display(uSub)
print('sigma_vm(0,h/2)=')
display(sigmavmSub1)
print('sigma_vm(L/2,-h/2)=')
display(sigmavmSub2)
print('sigma_vm(0,0)=')
display(sigmavmSub3)
print('sigma_vm(L/4,h/4)=')
display(sigmavmSub4)
print('A=')
display(ASub)

#Task 8

uFun       = lambdify([h,b_w], uSub)

sigmavmFun1 = lambdify([h,b_w], sigmavmSub1)
sigmavmFun2 = lambdify([h,b_w], sigmavmSub2)
sigmavmFun3 = lambdify([h,b_w], sigmavmSub3)
sigmavmFun4 = lambdify([h,b_w], sigmavmSub4)

AFun        = lambdify([h,b_w], ASub) 

#Task 9

n = 500 #number of points

val_h   = np.linspace(0.0001, h_max, n) # create the set of h 
val_b_w = np.linspace(0.0001, b_max, n) # create the set of b_w 

optVar_h, optVar_b_w = np.meshgrid(val_h, val_b_w) # meshgrid  two variables to have at n^2 points for calculation

mNum        = AFun(optVar_h, optVar_b_w)*valL*valro

# calculate the difference in displacement between the actual and the maximum allowed
uNum        = uFun(optVar_h, optVar_b_w)-u_lim


# calculate the difference in stress between the actual and the maximum allowed for every 4 points
sigmavmNum1  = sigmavmFun1(optVar_h, optVar_b_w)-sigma_y**2
sigmavmNum2  = sigmavmFun2(optVar_h, optVar_b_w)-sigma_y**2
sigmavmNum3  = sigmavmFun3(optVar_h, optVar_b_w)-sigma_y**2
sigmavmNum4  = sigmavmFun4(optVar_h, optVar_b_w)-sigma_y**2

#Task 10

plt.contourf(optVar_h, optVar_b_w, mNum) #plot for A
plt.colorbar()

plt.contour(optVar_h, optVar_b_w, uNum, 1, cmap='Greens') #displacement isoline

#stress isolines
plt.contour(optVar_h, optVar_b_w, np.sign(sigmavmNum1),1, cmap='Purples')
plt.contour(optVar_h, optVar_b_w, np.sign(sigmavmNum2),1, cmap='Reds')
plt.contour(optVar_h, optVar_b_w, np.sign(sigmavmNum3),1, cmap='Blues')
plt.contour(optVar_h, optVar_b_w, np.sign(sigmavmNum4),1, cmap='Oranges')




plt.xlabel(r'$h$')
plt.ylabel(r'$b_w$')

plt.xlim([0,h_max])
plt.ylim([0.,b_max])


plt.plot([0.,   h_max], [h_min,h_min], 'yellow',label='h_limits')
plt.plot([b_min,b_min], [0.,   b_max], 'yellow',label='b_limits')
plt.legend()
plt.show()