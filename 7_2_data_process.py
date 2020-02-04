import numpy as np
import matplotlib.pylab as plt

def generate_sample(realA=2.5,realB=-5):
	x_vals=np.linspace(0,10,100)#generate the real y
	y_reals=realA*x_vals+realB
	y_vals=y_reals+np.random.normal(0,1,100)#generate the virtual y
	plt.plot(x_vals,y_vals,'o',label='data') 
	plt.plot(x_vals,y_reals,'g-',label='real',linewidth=3)
    #plt.show()
	return x_vals,y_vals
def main():
	x,y=generate_sample()#get sample
	A=np.random.normal(0,1)
	B=np.random.normal(-5,5)
	batch_size=10
	times=1000
	losses=[]
	learning_rate=0.001
	print("init A={0},b={1}".format(A,B))
	for _ in range(times):
		rand_index=np.random.choice(len(x),size=batch_size)
		rand_x=x[rand_index]
		rand_y=y[rand_index]
		pred_y=A*rand_x+B
		loss=np.sum((pred_y-rand_y)*(pred_y-rand_y)/2)
		losses.append(loss)
		DLDA=np.sum((pred_y-rand_y)*rand_x)
		DLDB=np.sum(pred_y-rand_y)
		print(DLDA)
		A=A-learning_rate*DLDA
		B=B-learning_rate*DLDB
		pass
	x_show=np.linspace(0,1000,1000)
	x_v=np.linspace(0,10,100)
	y_v=A*x_v+B
	plt.plot(x_v,y_v,'r-',label='best',linewidth=3)
	#plt.plot(losses,'.',label='data',linewidth=1)
	print(A,B)
	plt.show()







if __name__=="__main__":
    main()
