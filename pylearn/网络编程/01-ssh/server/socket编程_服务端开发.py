import socket
import subprocess
#创建socket对象
socket_server = socket.socket()
#绑定ip地址和端口
socket_server.bind(("localhost",9999))
# 表示最多接受的客户端
socket_server.listen(5)
while True:
    #accept方法返回的是二元元组(链接对象,客户端对象)
    conn,address = socket_server.accept()
    #用链接对象来接受客户端发来的信息
    print(f"接收到的命令为:{address}")
    while True:
        cmd = conn.recv(1024).decode('utf-8')
        if cmd == 'exit':
            break
        res = subprocess.getoutput(cmd)
        length = str(len(res.encode()))
        print('cmd命令的长度为:',length)
        conn.send(length.encode('utf-8'))
        conn.send(res.encode("utf-8"))
    conn.close()
