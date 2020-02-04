import socket
while 1:
#1、创建服务端的socket对象
    server_socket = socket.socket()

#2、绑定一个ip和端口
    server_socket.bind(('172.16.201.161',91))

#3、服务器端一直监听是否有客户端进行连接
    print('waiting')
    
    server_socket.listen()

#4、如果有客户端进行连接、则接受客户端的连接
    clientSockt,addr =  server_socket.accept()   #返回客户端socket通信对象和客户端的ip

#5、客户端与服务端进行通信
    data = clientSockt.recv(1024).decode('utf-8')
    print('思文:%s'%(data))

#6、服务端给客户端回消息
    print('敝之：')
    speak=input()
    speak=bytes(speak,encoding='utf-8')
    clientSockt.send(speak)
#7、关闭socket对象
    clientSockt.close()    #客户端对象
    server_socket.close()  #服务端对象
