import socket
import cv2
import numpy as np
LOCAL_IP = '172.16.201.161'   #本机在局域网中的地址，或者写127.0.0.1
PORT = 91                   #指定一个端口
def server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket.AF_INET 指ipv4  socket.SOCK_STREAM 使用tcp协议
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #设置端口
    sock.bind((LOCAL_IP, PORT))       #绑定端口
    sock.listen(3)                    #监听端口
    while True:
        sc,sc_name = sock.accept()    #当有请求到指定端口是 accpte()会返回一个新的socket和对方主机的（ip,port）
        print('收到{}请求'.format(sc_name))
        infor = sc.recv(1024)       #首先接收一段数据，这段数据包含文件的长度和文件的名字，使用|分隔，具体规则可以在客户端自己指定
        print(infor)
        #length,file_name = infor.decode().split('|')
        if True:
            #newfile = open('image/'+str(random.randint(1,10000))+'.jpg','wb')  #这里可以使用从客户端解析出来的文件名
            #print('length {},filename {}'.format(length,file_name))
            sc.send(b'ok')   #表示收到文件长度和文件名
            #file = b''
            #total = int(length)
            get = 0
            while get < total:         #接收文件
                data = sc.recv(1024)
                #file += data
                get = get + len(data)
            print('应该接收{},实际接收{}'.format(length,len(file)))
            if file:
                print('acturally length:{}'.format(len(file)))
                newfile.write(file[:])
                newfile.close()
                sc.send(b'copy')    #告诉完整的收到文件了
        sc.close()
def server1():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket.AF_INET 指ipv4  socket.SOCK_STREAM 使用tcp协议
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #设置端口
    sock.bind((LOCAL_IP, PORT))       #绑定端口
    sock.listen(3)
    
    
        
    
if __name__=='__main__':
    server()
