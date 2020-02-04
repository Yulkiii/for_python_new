import code_source
import cv2
import numpy as np
import time

def main():
    clicked=False
    def onMouse(event,x,y,flags,param):
        global clicked
        if event==cv2.EVENT_LBUTTONUP:
            clicked=True
    cc1=cv2.VideoCapture('img/li13.avi')
    cv2.namedWindow('my')
    #cv2.resizeWindow('my',200,200)#改变窗口大小
    cv2.setMouseCallback('my',onMouse)
    print('showing camera feed ,click window or press any key to stop')
    success,frame=cc1.read()
    time1=time.time()
    count=0
    count1=0
    compare=[[0 ,0, 0],
      [0 ,0 ,0],
        [0 ,0 ,0],
            [0 ,0 ,0],
             [0 ,0 ,0]]
    #print(compare)
    while success and cv2.waitKey(1)==-1 and not clicked:
        count+=1
        if time.time()-time1>=1:
            time1=time.time()
            print('frames:',count)
            count=0
        count3=0
        #cv2.resizeWindow('my',640,360)
        x, y = frame.shape[0:2]
        frame2=cv2.resize(frame,((int(y/2)),(int(x/2))))#缩放
        frame3=cv2.resize(frame,((int(y/2)),(int(x/2))))#缩放
        frame2[:,:,0]=0
        frame2[:,:,2]=0
        frame4=frame2
        frame2=cv2.resize(frame,((int(y/2)),(int(x/2))))#缩放
        frame2[:,:,1]=0
        frame2[:,:,0]=0
        lower_blue=np.array([0,0,150])
        upper_blue=np.array([0,0,255])
        lower_blue3=np.array([0,150,0])
        upper_blue3=np.array([0,255,0])
        mask3=cv2.inRange(frame4,lower_blue3,upper_blue3)
        mask=cv2.inRange(frame2,lower_blue,upper_blue)
        subtracted2= cv2.subtract(mask,mask3)
        #gray=cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)#转灰度
        #ret,thresh1=cv2.threshold(gray,110,255,cv2.THRESH_BINARY)#直接二值化
        #th2 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,  cv2.THRESH_BINARY,3,5)
        #th3 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,3,5)
        #kernel = np.ones((5,5),np.uint8)
        #erosion = cv2.erode(th2,thresh1,iterations=1)
        #dilation = cv2.dilate(subtracted2,kernel,iterations=1)
        cv2.medianBlur(subtracted2,5)#中值滤波
        (cnts,_)=cv2.findContours(subtracted2,cv2.RETR_EXTERNAL,
                             cv2.CHAIN_APPROX_TC89_L1)
        
        #c=sorted(cnts,key=cv2.contourArea,reverse=False)[0]
        #rect=cv2.minAreaRect(c)
        #print(c[0])
        #frame= cv2.drawContours(frame3,cnts,-1,(225,0,0),2)
        #imgray=cv2.Canny(subtracted2,30,100)
        #imgray2=cv2.Canny(thresh1,30,100)
        compare=50000
        comparex1=1
        comparey1=1
        for i in range(0,len(cnts)):  
            x, y, w, h = cv2.boundingRect(cnts[i])
            #print((x+w)/2,(y+h)/2)
            if w*w+h*h>500 and w>20 and h>20:
                cv2.rectangle(frame3, (x,y), (x+w,y+h), (153,153,0),2)
                if w*w+h*h<=compare:
                    compare=w*w+h*h
                    comparex1=int(x+w/2)
                    comparey1=int(y+h/2)

        cv2.circle(frame3,(comparex1,comparey1),2,(0,255,0),2)
        '''

        circles = cv2.HoughCircles(imgray,cv2.HOUGH_GRADIENT,1,100,param1=100,param2=20,
                                   minRadius=20,maxRadius=80)#霍夫圆变换
    
        if  circles is None:
            print(type(circles))
        else:
            count1+=1
            print(circles)
            p=circles[0]#去掉circles数组一层外括号
            
            for i in p:   # 画出外圆
                if abs(compare[count3][0]-i[0])<=300:
                    cv2.circle(frame2,(i[0],i[1]),i[2],(0,255,0),2)
                #第二参数（）内是圆心坐标，第三参数是半径，第四参数（）内是颜色，第五参数是线条粗细
                # 画出圆心
                    cv2.circle(frame2,(i[0],i[1]),2,(0,0,255),3)
                count3+=1
            count3=0
            
            for i in p:
                compare[count3]=i
                count3+=1
                '''
        cv2.imshow('my',frame3)
        success,frame=cc1.read()
        #cv2.waitKey()
    cv2.destroyWindow('my')
    cc1.release()


    

if __name__=='__main__':
    main()
