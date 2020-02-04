'''
  ****************************(C) COPYRIGHT 2020 CCZU****************************
  * @file       myFormat.py
  * @brief      转浮点数为四字节，转四字节为浮点数
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
import struct
'''
/**************************************
@功能             四字节转浮点数
@调用关系           
@输入参数         h1~h4<256 and h1~h4>0
@返回值                float
@说明             
***************************************/
'''
def bytesToFloat(h1,h2,h3,h4):
    ba = bytearray()
    ba.append(h1)
    ba.append(h2)
    ba.append(h3)
    ba.append(h4)
    return struct.unpack("!f",ba)[0]
'''
/**************************************
@功能             浮点数转四字节
@调用关系           
@输入参数         float
@返回值           元组
@说明             
***************************************/
'''
def floatToBytes(f):
    bs = struct.pack("f",f)
    return (bs[3],bs[2],bs[1],bs[0])
