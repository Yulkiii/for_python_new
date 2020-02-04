import linecache
import tkinter
import hashlib
import numpy as np
import os
import matplotlib.pylab as plt
def main():
	a=[]
	f = open('mpu6500AngleData.txt', "r", encoding="utf-8")
	read=f.readlines()
	for i in range (len(read[0])-1):
		if read[0][i]=="-":
			b=''
			for j in range(4):
				if read[0][i+j+1]<='9' and read[0][i+j+1]>='0':
					b+=read[0][i+j+1]
			a.append(int(b))
	#file=open('3.txt','w')
	temp = np.array(a) 
	a=[]
	f = open('mpu6500AngleData.txt', "r", encoding="utf-8")
	read=f.readlines()
	for i in range (len(read[0])-1):
		if read[0][i]=="-":
			b=''
			for j in range(4):
				if read[0][i+j+1]<='9' and read[0][i+j+1]>='0':
					b+=read[0][i+j+1]
			a.append(int(b))
	temp2=np.array(a)
	y_vals=np.zeros(len(temp))
	x_vals=temp
	x_vals2=temp2
	y_vals2=np.ones(len(temp2))*0.2
	y_vals3=np.ones(len(temp2))*0.4
	temp3=np.zeros(len(temp2))
	print(a)
	'''
	for i in range (len(temp2)):
		a1=temp2[i]
		b1=np.argwhere(abs(temp-a1)<=4)
		if b1!=[]:
			temp3[i]=a1
	print(temp3)
	'''
	plt.plot(x_vals,y_vals,'.',label='data')
	plt.plot(x_vals2,y_vals2,'.',label='data')
	plt.plot(temp3,y_vals3,'.',label='data')
	plt.show()



    
    

if __name__ == '__main__':
	main()






