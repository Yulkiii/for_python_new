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
	U1=1
	P1=1
	Preal1=0
	uncertain1=1
	uncertain1h=1
	U2=1
	uncertain2=2
	uncertain2h=10
	for i in range(100):
		data.append(10*math.sin(2*Pi*i/100))
		dataOriginal.append(i*i/100+random.uniform(-1,1))
		Preal1=math.sqrt(uncertain1*uncertain1+P1*P1)
		Kg=Preal1*Preal1/(Preal1*Preal1+uncertain2*uncertain2)
		U1=U1+Kg*(dataOriginal[i]-U1)
		dataProcessed.append(U1)
		P1=math.sqrt((1-Kg)*Preal1*Preal1)
		uncertain2h+=(dataOriginal[i]-U1)*(dataOriginal[i]-U1)
		#uncertain2=uncertain2h/(i+1)
		if i>=1:
			uncertain1h+=(dataProcessed[i]-dataProcessed[i-1])*(dataProcessed[i]-dataProcessed[i-1])
			#uncertain1=uncertain1h/i
			error.append(uncertain1)


	plt.plot(dataOriginal,'.',label='data')
	plt.plot(dataProcessed,'-',label='data2')
	plt.plot(error,'-',label='data3')
	print(error)
	plt.show()




if __name__ == '__main__':
	main()