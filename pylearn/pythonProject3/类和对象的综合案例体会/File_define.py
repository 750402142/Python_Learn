import json

from pythonProject3.类和对象的综合案例体会.data_define import Record


class File:

    def read_data(self) ->list:
        pass

class File_read1(File):
    def __init__(self,path):
        self.path = path
    #复写
    def read_data(self) ->list:
        f= open(self.path,'r',encoding='utf-8')
        lines = f.readlines()
        record_lists:list[Record] = []
        for line in lines:
            line = line.replace("\n","")
            line_list = line.split(",")
            record = Record(line_list[0],line_list[1],int(line_list[2]),line_list[3])
            record_lists.append(record)
        f.close()
        return record_lists


class File_read2(File):
    def __init__(self,path):
        self.path = path
    def read_date(self) ->list:
        f = open(self.path,'r',encoding='utf-8')
        data = f.readlines()
        record_lists = []
        for line in data:
            line_dict = json.loads(line)
            record = Record(line_dict["date"],line_dict["order_id"],line_dict["money"],line_dict["province"])
            record_lists.append(record)
        f.close()
        return record_lists



if __name__ == "__main__":
    file_read1 = File_read1("D:\年1月销售数据.txt")
    # for record in file_read1.read_data():
    #     print(record)
    file_read2 = File_read2("D:\年2月销售数据JSON.txt")

