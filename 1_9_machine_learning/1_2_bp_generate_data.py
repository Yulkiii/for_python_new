import math
import json
import numpy as np
my_dir={}
def write_to_json():
    pass
def main():
    x=np.zeros((80,),dtype=np.float) 
    e=2
    for i in range(80):
        x[i]=(i-40)/20
    count=0
    f=x
    for i in range(8):
        data=f[i:i+10]
        my_dir[count]=list(data)
        count+=1
    f=x*x
    for i in range(8):
        data=f[i:i+10]
        my_dir[count]=list(data)
        count+=1
    f=e**x
    for i in range(8):
        data=f[i:i+10]
        my_dir[count]=list(data)
        count+=1
    f=np.sin(x)
    for i in range(8):
        data=f[i:i+10]
        my_dir[count]=list(data)
        count+=1
    f=np.cos(x)
    for i in range(8):
        data=f[i:i+10]
        my_dir[count]=list(data)
        count+=1
    f=x*x*x
    for i in range(8):
        data=f[i:i+10]
        my_dir[count]=list(data)
        count+=1
    f=x*np.sin(x)
    for i in range(8):
        data=f[i:i+10]
        my_dir[count]=list(data)
        count+=1
    f=x*np.cos(x)
    for i in range(8):
        data=f[i:i+10]
        my_dir[count]=list(data)
        count+=1
    f=x*x*np.sin(x)
    for i in range(8):
        data=f[i:i+10]
        my_dir[count]=list(data)
        count+=1
    f=x*x*np.cos(x)
    for i in range(8):
        data=f[i:i+10]
        my_dir[count]=list(data)
        count+=1
    f=x*x*x*np.sin(x)
    for i in range(8):
        data=f[i:i+10]
        my_dir[count]=list(data)
        count+=1
    f=x*x*x*np.cos(x)
    for i in range(8):
        data=f[i:i+10]
        my_dir[count]=list(data)
        count+=1
    f=1/(1+e**x)
    for i in range(8):
        data=f[i:i+10]
        my_dir[count]=list(data)
        count+=1
    f=1/(x+3)
    for i in range(8):
        data=f[i:i+10]
        my_dir[count]=list(data)
        count+=1
    print("done")
    with open("data1.json","w") as dump_f:
        json.dump(my_dir,dump_f)
    pass

if __name__=="__main__":
    main()