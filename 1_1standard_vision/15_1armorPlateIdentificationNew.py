#coding=utf-8
import cv2
import numpy as np
import mvsdk
import time
import math
import serial
import operator
ax=200
ay=200
def mouse_event(event, x,y,flags,param):
	if event==cv2.EVENT_LBUTTONDOWN:
		global ax
		global ay
		ax=x
		ay=y
def nothing(x):
	pass
def main_loop():
	# 枚举相机
	DevList = mvsdk.CameraEnumerateDevice()
	nDev = len(DevList)
	if nDev < 1:
		print("No camera was found!")
		return
	for i, DevInfo in enumerate(DevList):
		print("{}: {} {}".format(i, DevInfo.GetFriendlyName(), DevInfo.GetPortType()))
	i = 0 if nDev == 1 else int(input("Select camera: "))
	DevInfo = DevList[i]
	print(DevInfo)

	# 打开相机
	hCamera = 0
	try:
		hCamera = mvsdk.CameraInit(DevInfo, -1, -1)
	except mvsdk.CameraException as e:
		print("CameraInit Failed({}): {}".format(e.error_code, e.message) )
		return

	# 获取相机特性描述
	cap = mvsdk.CameraGetCapability(hCamera)

	# 判断是黑白相机还是彩色相机
	monoCamera = (cap.sIspCapacity.bMonoSensor != 0)

	# 黑白相机让ISP直接输出MONO数据，而不是扩展成R=G=B的24位灰度
	if monoCamera:
		mvsdk.CameraSetIspOutFormat(hCamera, mvsdk.CAMERA_MEDIA_TYPE_MONO8)
	else:
		mvsdk.CameraSetIspOutFormat(hCamera, mvsdk.CAMERA_MEDIA_TYPE_COLOR)

	# 相机模式切换成连续采集
	mvsdk.CameraSetTriggerMode(hCamera, 0)

	# 手动曝光，曝光时间20ms
	mvsdk.CameraSetAeState(hCamera, 0)
	mvsdk.CameraSetExposureTime(hCamera, 1* 1000)
	mvsdk.CameraSetSaturation(hCamera, 142)#saturation
	mvsdk.CameraSetContrast(hCamera, 150)#contrast
	mvsdk.CameraSetAnalogGain(hCamera,7)#Anolog gain
	mvsdk.CameraSetSharpness(hCamera,150)#sharpness
	mvsdk.CameraSetGain(hCamera,144,118,100)#color_gain
	mvsdk.CameraSetGamma(hCamera,50)#gamma
	#mvsdk.CameraSetWhiteLevel(hCamera, 1)#white balance
	# 让SDK内部取图线程开始工作
	mvsdk.CameraPlay(hCamera)
	# 计算RGB buffer所需的大小，这里直接按照相机的最大分辨率来分配
	FrameBufferSize = cap.sResolutionRange.iWidthMax * cap.sResolutionRange.iHeightMax * (1 if monoCamera else 3)
	# 分配RGB buffer，用来存放ISP输出的图像
	# 备注：从相机传输到PC端的是RAW数据，在PC端通过软件ISP转为RGB数据（如果是黑白相机就不需要转换格式，但是ISP还有其它处理，所以也需要分配这个buffer）
	pFrameBuffer = mvsdk.CameraAlignMalloc(FrameBufferSize, 16)
	count=0
	time1=time.time()
	a=0
	cv2.createTrackbar('case1:','Press q to end',0,100,nothing)
	cv2.createTrackbar('case2:','Press q to end',30,100,nothing)
	cv2.createTrackbar('case3:','Press q to end',109,200,nothing)
	ax2=ay2=0
	a2=cv2.getTrackbarPos('Saturation:','Press q to end')
	hsvv=100
	countc=0
	countc2=0
	x2=0
	y2=0
	areaLast=0
	areaThis=0#used for dynamic area Identification
	xThis=0
	yThis=0
	x2=0
	y2=0
	LA=[]
	aLA=0
	while (cv2.waitKey(1) & 0xFF) != ord('q'):
		portx="/dev/ttyUSB0"
		bps=115200#超时设置,None：永远等待操作，0为立即返回
		ser=serial.Serial(portx,bps,timeout=1)		
		b=cv2.getTrackbarPos('case1:','Press q to end')
		b2=cv2.getTrackbarPos('case2:','Press q to end')
		b3=cv2.getTrackbarPos('case3:','Press q to end')
		if time.time()-time1>=1:
			time1=time.time()
			print('frames:',count)
			print(a)
			count=0
			# 从相机取一帧图片
		try:
			count+=1
			pRawData, FrameHead = mvsdk.CameraGetImageBuffer(hCamera, 200)
			mvsdk.CameraImageProcess(hCamera, pRawData, pFrameBuffer, FrameHead)
			mvsdk.CameraReleaseImageBuffer(hCamera, pRawData)
			# 此时图片已经存储在pFrameBuffer中，对于彩色相机pFrameBuffer=RGB数据，黑白相机pFrameBuffer=8位灰度数据
			# 把pFrameBuffer转换成opencv的图像格式以进行后续算法处理
			frame_data = (mvsdk.c_ubyte * FrameHead.uBytes).from_address(pFrameBuffer)
			frame = np.frombuffer(frame_data, dtype=np.uint8)
			frame = frame.reshape((FrameHead.iHeight, FrameHead.iWidth, 1 if FrameHead.uiMediaType == mvsdk.CAMERA_MEDIA_TYPE_MONO8 else 3) )
			frame = cv2.resize(frame, (320+160+b*4,240+120+b*3), interpolation = cv2.INTER_LINEAR)
			frame=cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
			hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
			(B,G,R)=cv2.split(frame)
			frame2=frame
			cv2.setMouseCallback("Press q to end",mouse_event)
			if (cv2.waitKey(1) & 0xFF) == ord('c'):
				countc+=1
				name="pictures/bizhi"+str(countc)+".jpg"
				cv2.imwrite(name,frame)
				print('succeed!')
			if ax2!=ax:
				print('PIX:',ax,ay)
				print('BGR:',frame[ay,ax])
				print('HSV:',hsv[ay,ax])
			ax2=ax
			ay2=ay
			lower_green=np.array([0,0,160])#dark 0,80,25,light 0,105,25
			upper_green=np.array([60,60,255])#light56,255,109#dark20,100,40
			mask=cv2.inRange(frame,lower_green,upper_green)
			mask= cv2.Canny(mask, 120, 140)
			mask=cv2.blur(mask,(1,1))
			image,cnt,hierarchy = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
			allCountors=[]
			greatCountors=[]
			if(cnt):
				for i in range(0,len(cnt)):
					x,y,w,h=cv2.boundingRect(cnt[i])
					if y!=0 and w/h>=2:
						pass
					elif w*w+h*h>areaThis:
						areaThis=w*w+h*h
						
					if y!=0 and w/h>=2:
						pass
					elif w*w+h*h>=areaLast/1.3 and h/w>1.5 :#need to predict
						allCountors.append([x,y,w,h])
						cv2.rectangle(image,(x,y),(x+w,y+h),(153,153,0),1)
			for i in range(len(allCountors)):
				for j in range(len(allCountors)):
					if abs(allCountors[i][2]-allCountors[j][2])<=520 and abs(allCountors[i][3]-allCountors[j][3])<=520 and j>i :
						compare=abs(allCountors[i][2]-allCountors[j][2])+abs(allCountors[i][3]-allCountors[j][3])
						delta=abs(allCountors[i][0]-allCountors[j][0])
						greatCountors.append([compare,i,j,delta])
						x=allCountors[i][0]
						y=allCountors[i][1]
						x1=allCountors[j][0]
						y1=allCountors[j][1]
			greatCountors=sorted(greatCountors,key= operator.itemgetter(0))
			areaLast=areaThis
			areaThis=0
			best=0
			compareBest=100000
			if greatCountors:
				for i in range(3):
					if len(greatCountors)>i and greatCountors[i][3]<compareBest:
						compareBest=greatCountors[i][3]
						best=i
				LA.append(greatCountors[best][3])
			if len(LA)>6:
				LA.pop(0)
			aLA=sum(LA)/6
			if greatCountors and  greatCountors[best][3]<aLA+1:
				i=greatCountors[best][1]
				j=greatCountors[best][2]
				xThis=allCountors[i][0]+allCountors[i][2]/2+allCountors[j][0]+allCountors[j][2]/2
				yThis=allCountors[i][1]+allCountors[i][3]/2+allCountors[j][1]+allCountors[j][3]/2
				x2=xThis
				y2=yThis
			cv2.circle(frame2,(int(x2/2),int(y2/2)),3,(255,0,0),2)
			cv2.circle(image,(int(x2/2),int(y2/2)),3,(255,0,0),2)
			cen1=(240,180)
			cen1=(x2/2,y2/2)    
			######################################maping to real axis/unit: mm/radius of real round: 150/delta pitch:91/delta yaw:68
			rad1=15
                       
			'''
			P=240/4.8#density of pixels/unit: pixels*mm^-1
			D2=6#*1.31#the focal length
			Q2=91#delta pitch
			Q1=68#delta yaw
			Rreal=150
			D1=(Rreal/(rad1/P))*D2#get the real distance between len and object
			cenn0=int(cen1[0]-(Q1/D1)*6*P)
			cenn1=int(cen1[1]-(Q2/D1)*6*P)
			#cen1=(cenn0,cenn1)
			#print(D1,rad1)
			#print(cen1[1],cen1[0])
                        
			'''
			######################################send to mcuyaw,yaw28',pitch22'
			yawx=cen1[0]-240
			pitchy=180-cen1[1]
			yawAngle=math.atan(yawx/75/6.170323)*180/3.14159
			pitchAngle=math.atan(pitchy/75/6.170323)*180/3.14159
			#pitch38.39 yaw46.50
			intYawAngle=int(yawAngle*7.5+165+218+218)#218#+20
			intPitchAngle=int(pitchAngle*7.5+165)#165#35
			head=int(intYawAngle/64)#move right 6 bits,and get it
			tail=(intYawAngle-int(intYawAngle/64)*64)#get last 6 bits
			head=head+64#give flag bit "1" to first bit
			head=bytes(chr(head),encoding="utf-8")
			ser.write(head)
			time.sleep(0.0003)
			tail=bytes(chr(tail),encoding="utf-8")
			ser.write(tail)
			time.sleep(0.0003)
			head=int(intPitchAngle/64)#move right 6 bits,and get it
			tail=(intPitchAngle-int(intPitchAngle/64)*64)#get last 6 bits
			head=head+64#give flag bit "1" to first bit
			head=bytes(chr(head),encoding="utf-8")
			ser.write(head)
			time.sleep(0.0003)
			tail=bytes(chr(tail),encoding="utf-8")
			ser.write(tail)
			
			f=open("1_2date.txt",'a')
			s=str(x2/2)+"/"+str( y2/2)+" "
			f.write(s)
			f.close()
      
			
            #第二参数（）内是圆心坐标，第三参数是半径，第四参数（）内是颜色，第五参数是线条粗细
			cv2.imshow("img",mask)
			#cv2.imshow("Press q to end",frame2)
			name2="sendPitcures/bizhi"+".jpg"
			#cv2.imwrite(name2,frame2)#sudo chmod 666 /dev/ttyUSB0 
			
			
		except mvsdk.CameraException as e:
			if e.error_code != mvsdk.CAMERA_STATUS_TIME_OUT:
				print("CameraGetImageBuffer failed({}): {}".format(e.error_code, e.message) )





	# 关闭相机
	mvsdk.CameraUnInit(hCamera)

	# 释放帧缓存
	mvsdk.CameraAlignFree(pFrameBuffer)

def main():
	try:
		main_loop()
	finally:
		cv2.destroyAllWindows()
main()
#script -f output.txt
