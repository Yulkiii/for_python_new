import socket
import cv2
import numpy as np
address = ('172.16.201.161', 91)
def send1(photos):
    for photo in photos[0]:
        print('sending {}'.format(photo))
        #data = file_deal(photo)
        data=photo
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(address)
        sock.send(photo.encode())    #默认编码 utf-8,发送文件长度和文件名
        reply = sock.recv(1024)
        if 'ok' == reply.decode():             #确认一下服务器get到文件长度和文件名数据
            go = 0
            total = len(data)
            while go < total:                        #发送文件
                data_to_send = data[go:go + 1024]
                sock.send(data_to_send)
                go += len(data_to_send)
            reply = sock.recv(1024)
            if 'copy' == reply.decode():
                print('{} send successfully'.format(photo))
        sock.close()
        #由于tcp是以流的形式传输数据，我们无法判断开头和结尾，简单的方法是没传送一个文件，就使用一个socket，但是这样是消耗计算机的资源，博主正在探索更好的方法，有机会交流一下
'''      
def file_deal(file_path):    #读取文件的方法
    mes = 'b'
    try:
        file = open(file_path,'rb')
        mes = file.read()
    except:
        print('error{}'.format(file_path))
    else:
        file.close()
        return mes
        '''
def send(photo):
    #print('sending {}'.format(photo))
    #data = file_deal(photo)
    data=photo
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(address)
    sock.send(photo.encode())    #默认编码 utf-8,发送文件长度和文件名
    reply = sock.recv(1024)
    if 'ok' == reply.decode():             #确认一下服务器get到文件长度和文件名数据
        go = 0
        total = len(data)
        while go < total:                        #发送文件
            data_to_send = data[go:go + 1024]
            sock.send(data_to_send)
            go += len(data_to_send)
        reply = sock.recv(1024)
        if 'copy' == reply.decode():
            print('{} send successfully'.format(photo))
    sock.close()
    
def main():
    
    cc1=cv2.VideoCapture(1)
    success,frame=cc1.read()
    while success:
        send(frame)
        success,frame=cc1.read()
      
    
if __name__=='__main__':
    main();
