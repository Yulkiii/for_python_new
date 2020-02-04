import socket
while 1:
#1、创建socket通信对象
    clientSocket = socket.socket()

#2、使用正确的ip和端口去链接服务器
    clientSocket.connect(('172.16.201.161',91))

#3、客户端与服务器端进行通信
    # 给socket服务器发送信息
    print('思文：')
    speak=input()
    speak=bytes(speak,encoding="utf8")
    clientSocket.send(speak)
    print('waiting')

    # 接收服务器的响应(服务器回复的消息)
    recvData = clientSocket.recv(1024).decode('utf-8')
    print('敝之:\n%s'%(recvData))

#4、关闭socket对象
    clientSocket.close()
