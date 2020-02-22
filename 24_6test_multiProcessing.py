from  multiprocessing import Process,Pool,Manager,Value
import os, time,cv2,numpy

class Employee(object):
    def __init__(array):
        self.array=array
    def get(self):
        return self.array

def get_frame(num):
    clicked=False
    def onMouse(event,x,y,flags,param):
        global clicked
        if event==cv2.EVENT_LBUTTONUP:
            clicked=True
    cc1=cv2.VideoCapture(1)
    cv2.namedWindow('my')
    #cv2.resizeWindow('my',200,200)#改变窗口大小
    cv2.setMouseCallback('my',onMouse)
    print('showing camera feed ,click window or press any key to stop')
    success,frame=cc1.read()
    time1=time.time()
    count=0
    while success and cv2.waitKey(1)==-1 and not clicked:
        count+=1
        if time.time()-time1>=1:
            time1=time.time()
            print('frames:',count)
            count=0
        cv2.imshow('my',frame)
        success,frame=cc1.read()
        num.value+=1
    cv2.destroyWindow('my')
    cc1.release()


def put_number(num):
    while(num.value<300):
        print(num.value)
        time.sleep(1)

if __name__=='__main__':
    manager=Manager()
    number=Value("d",10.0)

    

    manager=Manager2()
    em=manager.Employee('zhangsan',1000)

    p=Process(target=get_frame,args=(number,))
    p.start()
    p1=Process(target=put_number,args=(number,))
    p1.start()
    p.join()
    p1.join()
    print(time.time())
    print(number)
    print('结束测试')