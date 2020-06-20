import numpy as np

import matplotlib.pylab as plt

import math

from sympy import *
def main():

    datas=np.array(

    [

    [199,200.2],

    [142.3,141.9],

    [173.8,172.8],

    [97.1,97.5],

    [121,118.8],

    [116.8,117.6],

    [106,105.4],

    [118,116.5],

    [142.0,140.8],

    [164,164],

    [193.6,193.8],

    [143,143],

    [135,134],

    [123.8,121.7],

    [110.7,110.6],

    [115.1,114.7],

    [141.7,139.9],

    [135,133.3],

    [148,147.2],

    [142,139.6],

    [112.3,111.7],

    [104.5,104.5],

    [105.4,106],

    [123.7,122.1],

    [123.7,122.1],

    [144.4,143.7],
    [152.3,151],
    [189.2,190.9],
    [46.7,48.15],
    [48.4,46.7],
    [27.2,25.8]

    ]

    )

    datas=datas.T

    plt.plot(datas[0],datas[0]-datas[1],".")

    plt.xlabel("test distance /cm")

    plt.ylabel("test distance subtracting real distance /cm")

    plt.show()


if __name__=="__main__":

    main()