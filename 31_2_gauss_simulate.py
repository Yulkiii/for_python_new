import math
import json
import numpy
import threading
import time
import matplotlib.pylab as plt
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
    #list1=[[1,2.3],[2.1,3],[2.9,4],[4,5.3],[5.1,6],[6.2,7.3],[7.2,9],[8,10],[8.8,11],[9.7,12]]
    #list2=[[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[7.3,9],[7.4,10]]
    #to use this class with trust =200,dimension=1,expect freq=100
    task1=predict(200,1,100)
    global pool
    global lock
    #read json file
    with open("myData3.json",'r') as load_f:
        load_dict = json.load(load_f)
    #threading start
    task1.start()
    last_time=0
    #store original data
    or_p=[]
    or_t=[]
    for i in load_dict:
        time.sleep((load_dict[str(i)][1]-last_time)/1000)
        lock.acquire()
        pool.append(load_dict[str(i)])
        lock.release()
        or_p.append(load_dict[str(i)][0])
        or_t.append(load_dict[str(i)][1])
        last_time=load_dict[str(i)][1]
    task1.join()
    #draw the graph
    plt.plot(time_1,predict_1,'.')
    plt.plot(or_t,or_p,'.')
    plt.plot()
    plt.show()

if __name__=="__main__":
    main()