import numpy as np

def main1():
    a=np.array(
    [[1,0,0],
    [2,1,0],
    [3,-2,1]])
    b=np.array(
    [[2,1,2],
    [0,1,-3],
    [0,0,-7]])
    d=np.array(
    [[2,1,2],
    [4,3,1],
    [6,1,5]])
    e=np.array(
    [[6.0,11.0,13.0]])
    e=e.T#转置
    f=np.linalg.inv(a)#矩阵逆运算
    c=np.dot(f,e)#乘法
    b=np.linalg.inv(b)
    c2=np.dot(b,c)
    print(c2)
    pass
def main2():
    a=np.array(
        [[2,-1,0],
        [-1,2,1],
        [0,-1,2]]
    )
    a=np.linalg.inv(a)
    b=np.array([[0,1,0]])
    b=b.T
    c=np.dot(a,b)
    print(c)
def main4():
    c=np.array([
        [1,0,0,0],
        [0,0.866,-0.5,10],
        [0,0.5,0.866,-20],
        [0,0,0,1]
    ])
    a=np.array([
        [0.866,-0.5,0,11],
        [0.5,0.866,0,-1],
        [0,0,1,8],
        [0,0,0,1]
    ])
    b=np.array([
        [0.866,-0.5,0,-3],
        [0.433,0.75,-0.5,-3],
        [0.25,0.433,0.866,3],
        [0,0,0,1]
    ])
    a=np.linalg.inv(a)
    d=np.dot(a,b)
    d=np.dot(d,c)
    d=np.linalg.inv(d)
    print(d)
def main():
    c=np.array([
        [1,0,0,0],
        [0,0.866,-0.5,10],
        [0,0.5,0.866,-20],
        [0,0,0,1]
    ])
    a=np.array([
        [0.866,-0.5,0,11],
        [0.5,0.866,0,-1],
        [0,0,1,8],
        [0,0,0,1]
    ])
    b=np.array([
        [0.866,-0.5,0,-3],
        [0.433,0.75,-0.5,-3],
        [0.25,0.433,0.866,3],
        [0,0,0,1]
    ])
    a=np.linalg.inv(a)
    d=np.dot(a,b)
    d=np.dot(d,c)
    d=np.linalg.inv(d)
    print(d)
def main3():
    b=np.array([
        [0.707,0.707,0,0],
        [-0.707,0.707,0,0],
        [0,0,1,0],
        [0,0,0,1]
    ])
    c=np.array([
    [11,9,9,11,11,9],
    [0,0,0,0,4,4],
    [0,0,2,2,0,0],
    [1,1,1,1,1,1]
    ])
    d=np.dot(b,c)
    print(d)



if __name__=="__main__":
    main()