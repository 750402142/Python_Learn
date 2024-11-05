import json
import os.path
import socket
import struct
import time


def put(socket_client,file):

    file_size = os.path.getsize(file)
    file_name = os.path.basename(file)
    params = {'file_size': file_size, 'file_name': file_name,'cmd':'put'}
    data = json.dumps(params).encode()
    # 先明确要发送数据的长度,接受固定长度的数据,解决粘包现象
    data_len_pack = struct.pack('i',len(data))
    socket_client.send(data_len_pack)
    socket_client.send(json.dumps(params).encode())
    with open(file, 'rb') as f:
        for line in f:
            socket_client.send(line)
    print('发送成功!')
def get(socket_client,file):
    params = {'file_name': file,'cmd': 'get'}
    data = json.dumps(params).encode()
    # 先明确要发送数据的长度,接受固定长度的数据,解决粘包现象
    data_len_pack = struct.pack('i', len(data))
    socket_client.send(data_len_pack)
    socket_client.send(json.dumps(params).encode())

    data_len_bytes = socket_client.recv(4)
    len_int = struct.unpack('i', data_len_bytes)[0]
    file_json = socket_client.recv(len_int)  # 首先收到的是json文件的字节文件
    params2 = json.loads(file_json.decode())  # 先由字节转换再由json文件转为字典
    file_size = params2['file_size']
    file_name = params2['file_name']
    path = f'image/{file_name}'
    # if not os.path.exists(os.path.dirname(path)):
    #     os.makedirs(os.path.dirname(path))
    receive_data_len = 0
    with open(path, 'wb') as f:
        while receive_data_len < file_size:
            temp = socket_client.recv(1024)
            f.write(temp)
            receive_data_len += len(temp)
    print('接受成功!')


#创建socket对象
socket_client = socket.socket()

socket_client.connect(("127.0.0.1", 9999))
print(f"Connected to server at {socket_client.getpeername()}")
while True:
    cmd_file = input("您要做的行为是(例如 put/get 文件名):")
    # 文件信息的处理
    cmd = cmd_file.split(' ')[0]
    file = cmd_file.split(' ')[1]
    if cmd == 'put':
        put(socket_client,file)
    elif cmd == 'get':
        get(socket_client,file)
    else :
        print('输入的命令不规范,请重新输入')





