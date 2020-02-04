import cv2
import numpy as np
import time

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
    count1=0
    compare=[[0 ,0, 0],
      [0 ,0 ,0],
        [0 ,0 ,0],
            [0 ,0 ,0],
             [0 ,0 ,0]]
    print(compare)
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
        
        lower_blue=np.array([50,184,50])
        upper_blue=np.array([180,225,180])
        
        mask=cv2.inRange(frame2,lower_blue,upper_blue)
        gray=cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)#转灰度
        ret,thresh1=cv2.threshold(gray,110,255,cv2.THRESH_BINARY)#直接二值化
        #th2 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,  cv2.THRESH_BINARY,3,5)
        #th3 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,3,5)
        kernel = np.ones((5,5),np.uint8)
        #erosion = cv2.erode(th2,thresh1,iterations=1)
        dilation = cv2.dilate(mask,kernel,iterations=1)
        imgray=cv2.Canny(dilation,30,100)
        #imgray2=cv2.Canny(thresh1,30,100)
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
                
        cv2.imshow('my',frame2)
        success,frame=cc1.read()
    cv2.destroyWindow('my')
    cc1.release()


    

if __name__=='__main__':
    main()
