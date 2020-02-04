import code_source
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
    while success and cv2.waitKey(1)==-1 and not clicked:
        count+=1
        portx="/dev/ttyUSB0"
        bps=115200#超时设置,None：永远等待操作，0为立即返回
        ser=serial.Serial(portx,bps,timeout=None)
        if time.time()-time1>=1:#display frame
            time1=time.time()
            count1+=1
            print('frames:',count)
            count=0
        x, y = frame.shape[0:2]


        frame2=cv2.resize(frame,((int(y/2)),(int(x/2))))
        framex=frame2
        lower_blue=np.array([20,100,10])
        upper_blue=np.array([80,160,100])
        mask=cv2.inRange(frame2,lower_blue,upper_blue)
        #cv2.medianBlur(mask,25)#中值滤波
        blur=cv2.GaussianBlur(mask,(5,5),0)#GaussianBlur
        (_,cnts,_)=cv2.findContours(blur,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_TC89_L1)
        compare=400000
        comparex1=1
        comparey1=1
       	cx2=cx1
       	cy2=cy1
       	anglex=0
       	angley=0
        for i in range(0,len(cnts)):  
            x, y, w, h = cv2.boundingRect(cnts[i])
            #print((x+w)/2,(y+h)/2)
            if w*w+h*h>4000 and w>20 and h>20:
                cv2.rectangle(framex, (x,y), (x+w,y+h), (153,153,0),2)
                if w*w+h*h<=compare:
                    compare=w*w+h*h
                    comparex1=int(x+w/2)
                    comparey1=int(y+h/2)
        cx1=comparex1
        cy1=comparey1
        anglex=int(((cx1-320)/640)*64)
       	angley=int(((cy1-180)/360)*40)
       	print((anglex+100+32),(angley+30+20))
       	
        result=ser.write(chr(anglex+100+32).encode("utf-16"))
        time.sleep(0.05)
        result=ser.write(chr(angley+30+20).encode("utf-16"))
        
        cv2.circle(framex,(int((cx1+cx2)/2),int((cy1+cy2)/2)),2,(0,0,255),2)
        	
        #print(comparex1,comparey1)
        #c=sorted(cnts,key=cv2.contourArea,reverse=False)[0]
        #frame2= cv2.drawContours(blur,cnts,-1,(225,0,0),2)                     
        cv2.imshow('my',framex)
        success,frame=cc1.read()
    cv2.destroyWindow('my')
    cc1.release()


if __name__=='__main__':
    main()
