'''
  ****************************(C) COPYRIGHT 2020 CCZU****************************
  * @file       main.py
  * @brief      定义接收类，定义发送类，定义串口查找函数，定义串口接收函数
  *             
  * @note       
  * @history
  *  Version    Date            Author          Modification
  *  V1.0.0    	2020/1/10       BIZHI           finished
  *
  @verbatim
  ==============================================================================

  ==============================================================================
  @endverbatim
  ****************************(C) COPYRIGHT 2020 CCZU****************************
  '''
import serial
import serial.tools.list_ports
import time
import myFormat
import CRC16
'''
/**************************************
@功能             接收类
@调用关系         内含generateStruct()函数，用于将接收数据转化
@输入参数         control,roboID,time,yawMotorSpeed,yawAbsoluteSpeed
@返回值           
@说明             roboID？
***************************************/
'''
class receive:
    def __init__(self,control=0,roboID=0,time=0,yawMotorSpeed=0.0,yawAbsoluteSpeed=0.0):
      self.control=control
      self.roboID=roboID
      self.time=time
      self.yawMotorSpeed=yawMotorSpeed
      self.yawAbsoluteSpeed=yawAbsoluteSpeed
    def generateStruct(self,data=[]):
    	if len(data==15):
    		self.control=data[2]
    		self.roboID=data[3]
    		self.time=data[4]
    		f=myFormat.bytesToFloat(data[5],data[6],data[7],data[8])
    		self.yawMotorSpeed=f
    		f=myFormat.bytesToFloat(data[9],data[10],data[11],data[12])
    		self.yawAbsoluteSpeed=f
'''
/**************************************
@功能             发送类
@调用关系         内含generateData()函数，用于将数据转化为8位无符号数
@输入参数         无
@返回值           
@说明             roboID？
***************************************/
'''
class send:
	def __init__(self,tx2Statu=0,fps=0,time=0,distance=0,pitchAngle=0.0,yawAngle=0.0):
		self.tx2Statu=tx2Statu
		self.fps=fps
		self.time=time
		self.distance=distance
		self.pitchAngle=pitchAngle
		self.yawAngle=yawAngle
	def generateData(self):
		data=[]
		data.append(0xAA)
		data.append(0x55)
		data.append(self.tx2Statu)
		data.append(self.fps)
		data.append(self.time)
		data.append(self.distance>>8)
		data.append(self.distance-self.distance>>8<<8)
		u8=myFormat.floatToBytes(self.pitchAngle)
		data.append(u8[0])
		data.append(u8[1])
		data.append(u8[2])
		data.append(u8[3])
		u8=myFormat.floatToBytes(self.yawAngle)
		data.append(u8[0])
		data.append(u8[1])
		data.append(u8[2])
		data.append(u8[3])
		data.append(0)
		data.append(0)
		CRC16.Append_CRC16_Check_Sum(data,17)
		return data
rData=receive(1,2,3,1.1,1.5)
sData=send(1,2,3,4,1.1,1.5)
'''
/**************************************
@功能             查找机器所有串口，可能Ubuntu与win10有异
@调用关系         
@输入参数         无
@返回值           所有串口代号
@说明             roboID？
***************************************/
'''
def finaPort_Name():
    port_list = list(serial.tools.list_ports.comports())
    if len(port_list) <= 0:
        print ("The Serial port can't find!")
    else:
        portname_list=[]
        for i in  list(port_list):
            port_list_0 = list(i)
            port_serial = port_list_0[0]
            portname_list.append(port_serial)
        print(portname_list)
        return  portname_list 
'''
/**************************************
@功能             收发数据
@调用关系         无
@输入参数         无
@返回值           无
@说明             先生成bytes发送给stm32，之后检验长度，开始帧，CRC16校验
***************************************/
'''
def receive_Portdata():
    while 1:
    	sBytes=[]
    	sBytes=sData.generateData()
    	portStr=[]
    	ser.write(sBytes)
    	str1 = ser.readline()
    	if str1 and len(str1)==15 and str1[0]==0xAA and str1[1]==0x55 and CRC16.myVerify_CRC16_Check_Sum(str1,15) and rData.time==sData.time:
    		print(str1)
    		break
    	time.sleep(0.5)
name =finaPort_Name()
ser = serial.Serial(port=name[1], baudrate=115200,timeout = 0.001)
    
def main():
    receive_Portdata()
    ser.close()
if __name__=="__main__":
    main()

#AA 55 AA 55 AA 55 AA 55 AA 55 AA 55 AA 55 55 CD 68
