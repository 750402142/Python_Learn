import json
import os
import socket
import subprocess
import struct
from fileinput import filename

#创建socket对象
socket_server = socket.socket()
#绑定ip地址和端口
socket_server.bind(("127.0.0.1", 9999))
# 表示最多接受的客户端
socket_server.listen(5)
# 设置两个循环是因为服务器不可能只为了一个客户端服务 当一个客服端停止的时候 继续等到新的客户端连接
while True:
    print('waiting for a connection')
    #accept方法返回的是二元元组(链接对象,客户端对象)
    conn,address = socket_server.accept()
    #用链接对象来接受客户端发来的信息
    data_len_bytes = conn.recv(4)
    len_int = struct.unpack('i',data_len_bytes)[0]
    file_json = conn.recv(len_int)# 首先收到的是json文件的字节文件
    file = json.loads(file_json.decode())# 先由字节转换再由json文件转为字典
    print('file:',file)
    file_size = file['file_size']
    file_name = file['file_name']
    path = f'image/{file_name}'
    # if not os.path.exists(os.path.dirname(path)):
    #     os.makedirs(os.path.dirname(path))
    receive_data_len = 0
    with open(path, 'wb') as f:
        while receive_data_len < file_size:
            temp = conn.recv(1024)
            f.write(temp)
            receive_data_len += len(temp)
    print('发送成功!')

