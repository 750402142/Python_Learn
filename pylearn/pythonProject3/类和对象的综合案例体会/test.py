import json

f= open("D:\年2月销售数据JSON.txt",'r',encoding='utf-8')
# lines = f.readlines()
# record_lists = []
# print(lines)
# for line in lines:
#     line = line.replace("\n","")
#     print(line)
#     line_list = line.split(",")
#     #record = Record(line_list[0],line_list[1],int(line_list[2]),line_list[3])
#     #record_lists.append(record)
#     print(line_list[1])
# f.close()

dicts = f.readlines()
#print(dicts)
for line in dicts:
    print(line)

