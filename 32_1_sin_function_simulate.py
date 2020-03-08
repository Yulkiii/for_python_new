import math
import json
import numpy
import threading
import time
import matplotlib.pylab as plt
import random
#store 
pool=[]
#store predicted position
predict_1=[]
#store predicted time
time_1=[]
#threading protected lock
lock=threading.Lock()
#to get Difference quotient of a list
def get_DQ(list1=[]):
    answers=[]
    next=list1
    new_next=[]
    while len(next)>1:
        new_next=[]
        for i in range(len(next)-1):
            temp=[]
            val=(next[i+1][0]-next[i][0])/(next[i+1][1]-next[i][1])
            temp.append(val)
            time1=(next[i+1][1]+next[i][1])/2
            temp.append(time1)
            new_next.append(temp)
            if i==len(next)-2:
                answers.append(round(val,4))
        next=new_next
    return answers
#class a class of predict ,with inherited class of threading,Thread
class predict(threading.Thread):
    #unit of od trust:microseconds,of freq:Hz,
    def __init__(self,trust,dimension,freq):
        threading.Thread.__init__(self)
        self.trust=trust
        self.dimension=dimension
        self.freq=freq
        self.piece=1000/freq
        self.thisTime=0
        self.last_time=0.0
        self.DQ=[]
        self.next_predict=0
        self.last_position=0
    def run(self):
        global pool
        global predict_1
        global lock
        while True:
            lock.acquire()
            for i in pool:
                if i[1]<self.thisTime-self.trust:
                    pool.pop(0)
                else :
                    break
            lock.release()
            length=len(pool)
            if len(pool)==0:
                self.go_error()
            elif pool[length-1][1]!=self.last_time:
                predict_1.append(pool[length-1][0])
                self.last_time=pool[length-1][1]
                self.last_position=pool[length-1][0]
                self.thisTime=self.last_time
                time_1.append(self.thisTime)
            else :
                self.DQ=get_DQ(pool)
                value=self.calculate()
                self.last_position+=value
                predict_1.append(self.last_position)
                time_1.append(self.thisTime)
            time.sleep(self.piece/1000)
            self.thisTime+=self.piece
    def go_error(self):
        print("out of time!")
        if len(predict_1)>10:
            exit(0)
    def calculate(self):
        predict_2=0
        size=len(self.DQ)
        for i in range(len(self.DQ)):
            predict_2=(predict_2+self.DQ[size-1-i])*self.piece
        return predict_2
def main():
    pi=3.1415926
    #to use this class with trust =200,dimension=1,expect freq=100
    task1=predict(400,1,100)
    global pool
    global lock
    #threading start
    task1.start()
    last_time=0
    time_2=0
    #store original data
    or_p=[]
    or_t=[]
    power=4000/2/pi
    for i in range(100):
        time_2+=80+random.random()
        time.sleep((time_2-last_time)/1000)
        value=math.sin(time_2/power)
        lock.acquire()
        pool.append([value,time_2])
        lock.release()
        or_p.append(value)
        or_t.append(time_2)
        last_time=time_2
    task1.join()
    #draw the graph
    differ=[]
    differ2=0
    for i in range(len(time_1)):
        value=math.sin(time_1[i]/power)
        differ1=abs(value-predict_1[i])
        differ2+=differ1
        differ.append(differ2)
    plt.plot(differ,'-')
    #plt.plot(time_1,predict_1,'.')
    #plt.plot(or_t,or_p,'.')
    plt.plot()
    plt.show()


if __name__=="__main__":
    main()