from socket import *
address='172.16.0.5'   #监听哪些网络  127.0.0.1是监听本机 0.0.0.0是监听整个网络
port=8080             #监听自己的哪个端口
buffsize=1024          #接收从客户端发来的数据的缓存区大小
s = socket(AF_INET, SOCK_STREAM)
s.bind((address,port))
s.listen(1)     #最大连接数
dict={"qwertyuiop":1}

print("Server Start!")
while True:
    clientsock,clientaddress=s.accept()
    print('connect from:',clientaddress)
#传输数据都利用clientsock，和s无关
    while True:
        recvdata=clientsock.recv(buffsize).decode('utf-8')
        if recvdata=='exit' or not recvdata:
            break
        senddata=recvdata+'from sever'
        print(senddata)
        if(senddata in dict):
            dict[senddata]=dict[senddata]-1
        clientsock.send(senddata.encode())
    clientsock.close()
s.close()
