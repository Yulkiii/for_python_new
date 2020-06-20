import numpy as np
import math
from sympy import *
def main():
    a=5
    x= symbols("x")
    rf1=x*x+sin(x)-2
    f1= diff(rf1,x)#get derivtive
    rf1 =  lambdify([x],rf1)#return to real function
    f1 =  lambdify([x],f1)
    while(1):
        x0=f1(a)
        x=rf1(a)
        org=np.array(
        [
            [a],
        ]
        )
        first=np.array(
        [
            [x],
        ]
        )
        m=np.array([
        [x0],
        ])
        m=np.linalg.inv(m)
        ans=np.dot(m,first)
        org=org-ans
        a=org[0][0]
        ans1=rf1(a)
        print(ans1,"|",a)
        i=input()

if __name__=="__main__":
    main()