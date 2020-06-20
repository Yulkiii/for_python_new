import numpy as np
import math
import sympy as sym
def main():
    pi=3.1415926535
    a=1.59
    b=1
    x,y=sym.symbols("x y")

    rf1=sym.cos(x)+sym.cos(x)*sym.cos(y)-sym.sin(x)*sym.sin(y)-1
    rf2=sym.cos(y)*sym.sin(x)+sym.sin(x)+sym.cos(x)*sym.sin(y)-1

    f1=sym.diff(rf1,x)#get derivtive
    f2=sym.diff(rf1,y)
    f3=sym.diff(rf2,x)
    f4=sym.diff(rf2,y)
    rf1 = sym.lambdify([x,y],rf1)#return to real function
    rf2 = sym.lambdify([x,y],rf2)
    f1 = sym.lambdify([x,y],f1)
    f2 = sym.lambdify([x,y],f2)
    f3 = sym.lambdify([x,y],f3)
    f4 = sym.lambdify([x,y],f4)

    while(1):
        
        x0=f1(a,b)
        x1=f2(a,b)
        y0=f3(a,b)
        y1=f4(a,b)
        x=rf1(a,b)
        y=rf2(a,b)
        org=np.array(
        [
            [a],
            [b],
        ]
        )
        first=np.array(
        [
            [x],
            [y],
        ]
        )
        m=np.array([
        [x0,x1],
        [y0,y1],
        ])
        m=np.linalg.inv(m)
        ans=np.dot(m,first)
        org=org-ans


        a=org[0][0]
        b=org[1][0]
        ans1=rf1(a,b)
        ans2=rf2(a,b)
        print(org,ans1,ans2)
        i=input()

if __name__=="__main__":
    main()