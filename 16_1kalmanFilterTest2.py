import threading
import linecache
import numpy 
import os
import matplotlib.pylab as plt
import time
import random
import math
import json
def main():
	dataOriginal=[]
	dataOriginal.append(0)
	count=0
	myDic={}
	for i in range(120):
		e=2.71828
		data1=20+e**(i/60)+random.normalvariate(0,0.2)
		dataOriginal.append(data1)
		myDic[count]=data1
		count+=1
	for i in range(60):
		e=2
		data1=26+e**(i/60)+random.normalvariate(0,0.1)
		dataOriginal.append(data1)
		myDic[count]=data1
		count+=1
	plt.plot(dataOriginal,'-',label='data')
	plt.xlabel("TIME\seconds")
	plt.ylabel("ANGLE\degrees")
	with open("myData.json","w") as f:
		json.dump(myDic,f)
	plt.show()




if __name__ == '__main__':
	main()