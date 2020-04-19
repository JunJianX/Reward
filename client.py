from socket import *
address='106.13.93.74'   #服务器的ip地址
port=8080           #服务器的端口号
buffsize=1024        #接收数据的缓存大小
s=socket(AF_INET, SOCK_STREAM)
s.connect((address,port))
while True:
    senddata=input('想要发送的数据：')
    if senddata=='exit':
        break
    s.send(senddata.encode())
    recvdata=s.recv(buffsize).decode('utf-8')
    print(recvdata)
s.close()