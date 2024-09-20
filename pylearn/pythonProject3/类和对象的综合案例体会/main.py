from pyecharts.options import TitleOpts

from pythonProject3.类和对象的综合案例体会.File_define import File_read1, File_read2
from pythonProject3.类和对象的综合案例体会.data_define import Record
from pyecharts.charts import Bar
file_text = File_read1("D:\年1月销售数据.txt")
file_json = File_read2("D:\年2月销售数据JSON.txt")
all_data = file_text.read_data() + file_json.read_date()
all_dict = {}
for record in all_data:
    #用来判断字典中该键值是否已经存在
    if record.date in all_dict.keys():
        all_dict[record.date] += record.money
    else:
        all_dict[record.date] = record.money
# print(all_dict)
keys = all_dict.keys()
bar = Bar()
money_list = []
bar.add_xaxis(list(keys))
bar.add_yaxis("销售额",list(all_dict.values()))
bar.set_global_opts(
    title_opts = TitleOpts(title = "每日销售额")
)
bar.render("每日销售额.html")
