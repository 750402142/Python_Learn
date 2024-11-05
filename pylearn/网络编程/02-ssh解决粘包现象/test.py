import struct
lens = struct.pack('i',100)
print(len(lens))
print(struct.unpack('i',lens)[0])