# Optimization the cross-sectional geometry of a double - clamped beam
Consider the double-clamped beam with a distributed load. The cross section is constructed with two parabolic curves in the form ***b(y)*** that depend on ***b<sub>t</sub>, b<sub>w</sub>*** and ***h***. Distributed load has a parabolic shape ***p(x)*** that depend on the ***p<sub>max</sub>, p<sub>min</sub>*** and ***L***. The Young's modulus of the material is ***E***, the yiels stress is ***σ<sub>y</sub>*** and the deflection is ***u(x)***. 

![image](https://user-images.githubusercontent.com/89813720/194971716-1ac941a8-9e12-453e-9e7c-619f41197742.png)

# Task 1. Derivation the area ***A(y)***, the first moment of area ***Q(y)*** and the second moment of area ***I(y)***

As we can see our cross-sectional area is symmetric. It means that we can integrate ***A(y)*** from ***0*** to ***h/2*** but need to multiply by ***2***.

![image](https://user-images.githubusercontent.com/89813720/194971819-2f12612c-085d-469c-8e03-49d12bf49d15.png)

Define ***b(y)***:
We have parabolic shapes. The main equation for a parabola is
***x =ay<sup>2</sup>+by+c***, where ***a,b,c*** are constants that need to be defined. Using ‘boundary’ conditions: 

If ***y=0*** then ***x=b<sub>w</sub>***

If ***y=h/2*** then ***x=b<sub>f</sub>***

If ***y=-h/2*** then ***x=b<sub>f</sub>***

Substitute these conditions to parabolic equation we can obtain that:
 ***a=4(b<sub>f</sub>-b<sub>w</sub> )/h<sup>2</sup> ,  b=0,c=b<sub>w</sub>***

The same consideration should be made for the second moment of inertia. We need to multiply our integral by ***2***, because our cross-sectional area is symmetric through the axis ***y***.

# Task 2. Governing ODE equation

The governing equation for the beam is 

![image](https://user-images.githubusercontent.com/89813720/195144101-d7c49f4a-02a9-4fb0-8fa5-43ee4604d873.png)

Derivation of the parabolic shape of ***p(x)***. The main equation for parabola is p =ax^2+bx+c, where ***a,b,c*** are constants that need to be defined. Using ‘boundary’ conditions: 

If ***x=L/2*** then ***p=p<sub>max</sub>***

If ***x=0*** then ***p=p<sub>min</sub>***

If ***x=L*** then ***p=p<sub>min</sub>***

Substitute these conditions to parabolic equation we can obtain that:
 ***a=(-4(p<sub>max</sub>-p<sub>min</sub>))/L<sup>2</sup>*** ,  ***b=4(p<sub>max</sub>-p<sub>min</sub>)/L, c=p<sub>min</sub>***
 
# Task 3. Derivation the general solution to the governing ODE

We solve the ODE in symbolic equation with corresponding constants ***C1, C2, C3, C4***.

# Task 4. State the boundary conditions

For this case the beam has two fixed walls. It means that displacemnet on the ends equals to zero (fixed) and slope equals to zero. 

![image](https://user-images.githubusercontent.com/89813720/195144321-4ba6a47b-2270-4411-b73c-c9883f971143.png)

# Task 5. Calculate the integration constants

We can substitute boundary conditions in our equation and can obtain the solution for displacement for simply supported beam. 

# Task 6. Derivation the moment, shear and square of the von mises stress 

We use the following equations:

![image](https://user-images.githubusercontent.com/89813720/195144391-bb4ad757-86e7-404c-be30-87b4bf3b2eca.png)

We can substitute derivatives of displacement in our equation and can obtain moment, shear force and stresses.

**Optimization criteria**

The first optimization criteria mean that we want to construct and design a minimum-mass simply supported beam. This is important from economic point of view. The mass is proportional to the cross-sectional area because length and density are fixed in our case. ***m=ρV=ρAL***. 

The second optimization criteria mean there is a stress constraint. By varying the ***b<sub>w</sub>***  and ***h*** in the beam we don’t want to exceed a maximum stress constraint (***σ<sub>y</sub>***). But in this case, we have shear and normal stresses, that’s why we want to minimize Von-Mises stress (combination of ***σ<sub>xx</sub>*** and ***σ<sub>xy</sub>***). Otherwise, we will face the problem of beam destruction. 

Third optimization criteria mean there is a deflection constraint. This is one of the important limitations. In real design, it is very important to minimize the maximum deflection with a certain value. Otherwise, we can run into the problem of the destruction of the structure. 

The fifth and sixth optimization criteria mean that in the construction of beam (manufacture) there are dimension restrictions, that width or height shouldn’t be greater than the certain values that are used in production during manufacture.

# Task 7. Substitution the constants in the above equation

![image](https://user-images.githubusercontent.com/89813720/195144624-ea72ede0-6aa6-4a52-b621-37bcede906f6.png)

![image](https://user-images.githubusercontent.com/89813720/195144710-1f49265a-ea32-426a-a828-2d3c1c124354.png)


It is obvious from the symmetry of the problem since the distributed load is symmetrical the maximum deflection will be in the middle of the beam i.e. ***x=L/2***.
To find the maximum stress we can consider four points. 
To find the maximum stress in fact we need to understand where the Von-Mises stress is maximum. The greater contribution in Von-Mises stress is made by the normal stress, because: ***σ<sub>vm</sub><sup>2</sup>=σ<sub>xx</sub><sup>2</sup>+3σ<sub>xy,</sub><sub>max</sub>***. Therefore we can simplify our problem in the form of considering a rectangular distribution load.
Then the maximum moment is equal to: 
***M<sub>ends,max</sub>=(wL<sup>2</sup>)/12***.  It is obvious that the maximum will be at point ***x=0*** and ***x=L***.
At the same time y should be equal to ***–h/2***: ***y=-h/2*** to obtain the maximum normal stress, and then to obtain the maximum Von-Misses stress. 
Substitute all the constants in the solution.

# Task 8. Lambfify operation into Python function definition

# Task 9. Generate the meshgrid of the tes pounts

Meshgrided ***n<sup>2</sup>*** points and generated values for the mass, the displacement and the stress constraints. 

# Task 10. Plot the optimization objective a filled cotour plot

Plot the optimization objective a filled cotour plot

![image](https://user-images.githubusercontent.com/89813720/195145078-8f5ac670-a1c1-48a8-aa9c-0e814fc42f35.png)

In the figure, two yellow lines are visible which restrictions for ***b<sub>w</sub>*** and ***h*** are. 

![image](https://user-images.githubusercontent.com/89813720/195145169-b22686e0-fc31-4243-8883-77ed3ad0c2f4.png)

![image](https://user-images.githubusercontent.com/89813720/195145246-c705de54-c220-40f4-bd14-a13ba57be971.png)


This figure shows an approximation for displacement isoline. Here I had to zoom the previous graph because displacement isoline is not visible.  Displacement isoline is out of bounds for h and bw.

![image](https://user-images.githubusercontent.com/89813720/195145361-a1970e9a-8788-4bd0-81de-ab1bef15afd0.png)

At this point, we have the maximum moment. So in this case we will get the correct solution for an optimization problem. The red arrows show a feasible area. The area indicated by the orange arrow satisfies all the conditions and is in the feasible area. So we can choose optimizing dot. The rod dot will be optimized for this case because we are looking at the area to the right of the purple line, and the contour for the mass has the smallest value. 

[***h=0.23, b<sub>w</sub>=0.1***]

