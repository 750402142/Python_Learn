import socket

#创建socket对象
socket_client = socket.socket()

socket_client.connect(("localhost",9999))
while True:
    cmd = input("您要向服务端发送的命令为:")
    socket_client.send(cmd.encode("utf-8"))
    if cmd == "exit":
        break
    length_bytes = socket_client.recv(1024)
    length = int(length_bytes.decode('utf-8'))
    lens = 0
    for i in range(0,length,1024):
        res = socket_client.recv(1024)
        lens += len(res)

    print('接收到的命令长度为:',lens)
print('该客户端已关闭')
socket_client.close()
