import json
#打开文件
f = open("D:\pylearn\work\datas.txt",'r',encoding='utf-8')
#读取文件并将文件转为为python语言下的列表
datas = json.loads(f.read())
#print(datas)
#定义一个用来提取省份的函数
def get_province(data:list):
    if data[1][0:2] == '新疆':
        return data[1][0:2]
    else:
        return data[1][0:3]
#得到每一个省份并去重
provinces = set((map(get_province,datas)))
#print(provinces)
dicts = {}
for province in provinces:
    # data_province = list(filter(lambda a:))
    #过滤出和province对应的数据
    data_province = list(filter(lambda data: get_province(data) == province, datas))
    #将键和值同时加入到字典dicts中
    dicts[province] = data_province
print(dicts)
#打印出每一个键值
for key in dicts.keys():
     print(key)