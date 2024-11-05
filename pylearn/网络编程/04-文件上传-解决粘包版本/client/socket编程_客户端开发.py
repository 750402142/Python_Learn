import json
import os.path
import socket
import struct
import time

#创建socket对象
socket_client = socket.socket()

socket_client.connect(("127.0.0.1", 9999))
print(f"Connected to server at {socket_client.getpeername()}")
while True:
    cmd = input("您要做的行为是(例如 put 文件名):")
    # 文件信息的处理
    file = cmd.split(' ')[1]
    file_size = os.path.getsize(file)
    file_name = os.path.basename(file)
    file_params = {'file_size': file_size, 'file_name': file_name}
    data = json.dumps(file_params).encode()
    # 先明确要发送数据的长度,接受固定长度的数据,解决粘包现象
    data_len_pack = struct.pack('i',len(data))
    socket_client.send(data_len_pack)
    socket_client.send(json.dumps(file_params).encode())
    with open(file, 'rb') as f:
        for line in f:
            socket_client.send(line)
    print('发送成功!')



