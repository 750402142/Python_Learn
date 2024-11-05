import json
import os
import struct
file = './client/media/宫园薰.jpg'
file_size = os.path.getsize(file)
file_name = os.path.basename(file)
file_dict = {'file_name': file_name, 'file_size': file_size}
print(struct.pack('s',json.dumps(file_dict).encode()))