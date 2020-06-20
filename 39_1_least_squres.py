import numpy as np
e=2.71828

def main1():
    a=np.array(
    [
    [1,1/e],
    [1,0],
    [1,e*e],
    [4,e]
    ]
    )
    aT=a.T
    b=np.array(
    [[2,3,9,5]])
    b=b.T

    b=np.dot(aT,b)
    a=np.dot(aT,a)

    a=np.linalg.inv(a)
    ans=np.dot(a,b)
    print(a)

    print(ans)
    exit(0)
    pass
def main():
    a=np.array(
    [
    [0,0,0,0,1],
    [16*16,16*4,4*4,4,1],
    [1,1,1,1,1],
    [32,12,2,1,0],
    [4,3,1,1,0]
    ])
    b=np.array(
    [[1,0,0,0,1]])
    b=b.T

    a=np.linalg.inv(a)
    ans=np.dot(a,b)
    print(a)

    print(ans)


if __name__=="__main__":
    main()