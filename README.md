# Optimization the cross-sectional geometry of a doubly clamped beam
Consider the doubly clamped beam with distributed load. The cross section is constructed with two parabolic curves in the form b(y) that depend on b_t, b_w,h. Distributed load has a parabolic shape p(x) that depend on the p_max, p_min and L. The Young's modulus of the material is E, the yiels stress is sigma_y and the deflection is u(x). 

**Task 1. Derivation the area A(y), the first moment of area Q(y) and the second moment of area I(y)**

As we can see our cross-sectional area is symmetric. It means that we can integrate A(y) from 0 to h/2 but need to multiply by 2.

Define b(y):
We have parabolic shapes. The main equation for a parabola is
x =ay^2+by+c, where a,b,c are constants that need to be defined. Using ‘boundary’ conditions: 

If y=0 then x=b_w
If y=h/2 then x=b_f
If y=-h/2 then x=b_f

Substitute these conditions to parabolic equation we can obtain that:
 a=4(b_f-b_w )/h^2 ,  b=0,c=b_w

The same consideration should be made for the second moment of inertia. We need to multiply our integral by 2, because our cross-sectional area is symmetric through the axis y.

**Task 2. Governing ODE equation**

The governing equation for the beam is 

EIy^''''-p(x)=0
Derivation of the parabolic shape of p(x). The main equation for parabola is p =ax^2+bx+c, where a,b,c are constants that need to be defined. Using ‘boundary’ conditions: 
If x=L/2 then p=p_max
If x=0 then p=p_min
If x=L then p=p_min

Substitute these conditions to parabolic equation we can obtain that:
 a=(-4(p_max-p_min ))/L^2 ,  b=4(p_max-p_min )/L,c=p_min
 
**Task 3. Derivation the general solution to the governing ODE**

We solve the ODE in symbolic equation with corresponding constants C2, C2, C3, C4

**Task 4. State the boundary conditions**

For this case the beam has two fixed walls. It means that displacemnet on the ends equals to zero (fixed) and slope equals to zero. 

**Task 5. Calculate the integration constants**

We can substitute boundary conditions in our equation and can obtain the solution for displacement for simply supported beam. 

**Task 6. Derivation the moment, shear and square of the von mises stress **

We use the following equations:

We can substitute derivatives of displacement in our equation and can obtain moment, shear force and stresses.

**Optimization criteria**

The first optimization criteria mean that we want to construct and design a minimum-mass simply supported beam. This is important from economic point of view. The mass is proportional to the cross-sectional area because length and density are fixed in our case. m=ρV=ρAL. 
The second optimization criteria mean there is a stress constraint. By varying the b_w  and h in the beam we don’t want to exceed a maximum stress constraint (σ_y). But in this case, we have shear and normal stresses, that’s why we want to minimize Von-Mises stress (combination of σ_xx  and σ_xy). Otherwise, we will face the problem of beam destruction. 
Third optimization criteria mean there is a deflection constraint. This is one of the important limitations. In real design, it is very important to minimize the maximum deflection with a certain value. Otherwise, we can run into the problem of the destruction of the structure. 
The fifth and sixth optimization criteria mean that in the construction of beam (manufacture) there are dimension restrictions, that width or height shouldn’t be greater than the certain values that are used in production during manufacture.

**Task 7. Substitution the constants in the above equation**

It is obvious from the symmetry of the problem since the distributed load is symmetrical the maximum deflection will be in the middle of the beam i.e. x=L/2.
To find the maximum stress we can consider 4 points. 
To find the maximum stress in fact we need to understand where the Von-Mises stress is maximum. The greater contribution in Von-Mises stress is made by the normal stress, because: σ_vm^2=σ_xx^2+〖3σ〗_xy^2. Therefore we can simplify our problem in the form of considering a rectangular distribution load.
Then the maximum moment is equal to: 
M_(ends max)=(wL^2)/12.  It is obvious that the maximum will be at point x=0 and x=L.
At the same time y should be equal to –h/2 : y=-h/2 to obtain the maximum normal stress, and then to obtain the maximum Von-Misses stress. 
Substitute all the constants in the solution.

**Task 8. Lambfify operation into Python function definition**

**Task 9. Generate the meshgrid of the tes pounts**

**Task 10. Plot the optimization objective a filled cotour plot**

Plot the optimization objective a filled cotour plot

In the figure, two yellow lines are visible which restrictions for b_w and h are. 
σ_vm^2 (0,h/2)-σ_y^2→PURPLE
σ_vm^2 (L/2,-h/2)-σ_y^2→RED
σ_vm^2 (0,0)-σ_y^2→BLUE
σ_vm^2 (L/4,h/4)-σ_y^2→ORANGE 

This figure shows an approximation for displacement isoline. Here I had to zoom the previous graph because displacement isoline is not visible.  Displacement isoline is out of bounds for h and bw.
𝜎𝑣𝑚20,ℎ2−𝜎𝑦2→𝑃𝑈𝑅𝑃𝐿𝐸. At this point, we have the maximum moment. So in this case we will get the correct solution for an optimization problem. The red arrows show a feasible area. The area indicated by the orange arrow satisfies all the conditions and is in the feasible area. So we can choose optimizing dot. The rod dot will be optimized for this case because we are looking at the area to the right of the purple line, and the contour for the mass has the smallest value. [ℎ=0.23,𝑏𝑤=0.1]




