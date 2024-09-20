from pyecharts.charts import Bar
from pyecharts.options import LabelOpts

f= open("D:\年1月销售数据.txt",'r',encoding='utf-8')
#使用readlines()生成列表
lines = f.readlines()
#先把列表中的日期从小到大排列一遍
lines.sort(reverse=False)
data_list = []
for line in lines:
    line_list = line.split(",")
    line_list[0].replace("-","/")
    line_list[2] = int(line_list[2])
    data_list.append(line_list)

#print(lines)
#print(data_list)
#统计所有的一日的销售额度
dicts = {}
for data in data_list:
    try:
       dicts[data[0]].append(data[2])
    except KeyError:
        dicts[data[0]] = []
        dicts[data[0]].append(data[2])
# print(dicts)
keys = dicts.keys()

bar = Bar()
money_list = []
for key in keys:
    sum_money = 0
    bar.add_xaxis(key)
    for data in dicts[key]:
        sum_money += data
    money_list.append(sum_money)
bar.add_yaxis("销售额",money_list,label_opts=LabelOpts(is_show=False))
bar.render("每一日的销售额.html")




