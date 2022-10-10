# optimization-the-cross-sectional-geometry-of-a-doubly-clamped-beam-
Consider the doubly clamped beam with distributed load. The cross section is constructed with two parabolic curves in the form b(y) that depend on b_t, b_w,h. Distributed load has a parabolic shape p(x) that depend on the p_max, p_min and L. The Young's modulus of the material is E, the yiels stress is sigma_y and the deflection is u(x). 

#Task 1. Derivation the area A(y), the first moment of area Q(y) and the second moment of area I(y)

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

Task 2. Governing ODE equation 

The governing equation for the beam is 

EIy^''''-p(x)=0
Derivation of the parabolic shape of p(x). The main equation for parabola is p =ax^2+bx+c, where a,b,c are constants that need to be defined. Using ‘boundary’ conditions: 
If x=L/2 then p=p_max
If x=0 then p=p_min
If x=L then p=p_min

Substitute these conditions to parabolic equation we can obtain that:
 a=(-4(p_max-p_min ))/L^2 ,  b=4(p_max-p_min )/L,c=p_min
 
 Task 3.

