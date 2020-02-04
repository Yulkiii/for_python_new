
import cv2
import numpy as np
import time
import serial
import math

def main():
    clicked=False
    def onMouse(event,x,y,flags,param):
        global clicked
        if event==cv2.EVENT_LBUTTONUP:
            clicked=True
    cc1=cv2.VideoCapture('img/li15.webm')
    cc1=cv2.VideoCapture(3)
    cv2.namedWindow('my')
    cv2.setMouseCallback('my',onMouse)
    print('showing camera feed ,click window or press any key to stop')
    success,frame=cc1.read()
    time1=time.time()
    count=0
    count1=0
    cx1=0
    cx2=0
    cy1=0
    cy2=0
    countx=0
    while success and cv2.waitKey(1)==-1 and not clicked:
        count+=1
        portx="/dev/ttyUSB0"
        bps=9600#超时设置,None：永远等待操作，0为立即返回
        ser=serial.Serial(portx,bps,timeout=None)
        countx+=1;
        if(countx>=20):
            countx==20
        if time.time()-time1>=1:#display frame
            time1=time.time()
            count1+=1
            print('frames:',count)
            count=0      
        x, y = frame.shape[0:2]
        #frame2=cv2.resize(frame,((int(y/2)),(int(x/2))))
        #print(y/2,x/2)
        #print(comparex1,comparey1)
	#sudo chmod 666 /dev/ttyUSB0                    
        cv2.imshow('my',frame[650:720,400:760])
        color=((frame[400,650]/5+frame[719,650]/5+frame[400,719]/5+frame[700,719]/5+frame[719,525]/5)+(frame[400,640]/5+frame[719,640]/5+frame[400,709]/5+frame[700,709]/5+frame[719,505]/5))/2
        if(countx>=20):
            if(color[0]>=120 and color[0]<=160 and color[1]>180 and color[1]<220 and color[2]<=200):
                print("green")
                ser.write(chr(1).encode("utf-16"))
            elif(color[0]>=210 and color[1]>210 and color[2]>=200):
                print("white")
                ser.write(chr(2).encode("utf-16"))
            else:
                print("empty")
                ser.write(chr(0).encode("utf-16"))
        print(color)
        
        
        success,frame=cc1.read()
    cv2.destroyWindow('my')
    cc1.release()


if __name__=='__main__':
    main()
