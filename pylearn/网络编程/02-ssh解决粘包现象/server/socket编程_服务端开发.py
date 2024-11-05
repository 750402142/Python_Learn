import socket
import subprocess
import struct
#创建socket对象
socket_server = socket.socket()
#绑定ip地址和端口
socket_server.bind(("localhost",9999))
# 表示最多接受的客户端
socket_server.listen(5)
# 设置两个循环是因为服务器不可能只为了一个客户端服务 当一个客服端停止的时候 继续等到新的客户端连接
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
        length = len(res.encode())
        # 将长度压缩为固定的四个字节,这样在客户端就可以设置固定的4来接受
        length_bytes = struct.pack('i',length)
        print('cmd命令的长度为:',length)
        conn.send(length_bytes)
        conn.send(res.encode("utf-8"))
    conn.close()
