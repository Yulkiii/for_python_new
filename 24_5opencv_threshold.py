import cv2
import numpy
import time
import threading
'''
def main():
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
    cv2.destroyWindow('my')
    cc1.release()
'''
count2=0

class myThread (threading.Thread):   #继承父类threading.Thread
    def __init__(self):
        threading.Thread.__init__(self)
    def get_pic(self):
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
            count2+=1
            if time.time()-time1>=1:
                time1=time.time()
                print('frames:',count)
                count=0
            cv2.imshow('my',frame)
            success,frame=cc1.read()
        cv2.destroyWindow('my')
        cc1.release()

class myThread2 (threading.Thread):   #继承父类threading.Thread
    def __init__(self):
        threading.Thread.__init__(self)
    def put_num(self):
        while(count2<100):
            print(count2)
            time.sleep(1)

def main():
    thread1 = myThread()
    thread2 = myThread2()
    # 开启线程
    thread1.start()
    thread2.start()
    print("1")



if __name__=="__main__":
    main()