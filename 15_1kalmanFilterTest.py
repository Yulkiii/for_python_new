import threading
import linecache
import numpy as np
import os
import matplotlib.pylab as plt
import time
import random
import math
def main():
	dataOriginal=[]
	dataProcessed=[]
	data=[]
	error=[]
	Pi=3.1415926535
	P=10
	R=100
	Rh=0
	Q=1
	Qh=0
	X=0
	for i in range(300):
		K=P/(P+R)
		data.append(10*math.sin(2*Pi*i/100))
		dataOriginal.append(10*math.sin(2*Pi*i/100)+random.uniform(-1,1))
		X=X+K*(dataOriginal[i]-X)
		Qh+=((dataOriginal[i]-X)*(dataOriginal[i]-X))
		error.append(Q)
		dataProcessed.append(X)
		#Q=Qh/(i+1)
		if i>=1:
			Rh+=((dataProcessed[i]-dataProcessed[i-1])*(dataProcessed[i]-dataProcessed[i-1]))
			Q=Rh/i
		
		P=(1-K)*P+Q

	plt.plot(dataOriginal,'.',label='data')
	plt.plot(dataProcessed,'-',label='data2')
	plt.plot(error,'-',label='data3')
	print(error)
	plt.show()




if __name__ == '__main__':
	main()
