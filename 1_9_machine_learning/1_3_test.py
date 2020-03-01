import math
import json
import numpy as np
my_dir={}
def main():
    with open('data1.json', encoding='utf-8') as f:
        line = f.readline()
        d = json.loads(line)
    list1=d["0"]
    listAh=list1[0:9]
    listAf=list1[9]
    listAh=np.asarray(listAf) 
    listAf=np.asarray(listAf) 
    print(listAh)
    print(listAf)


if __name__=="__main__":
    main()