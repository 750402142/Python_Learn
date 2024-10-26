import pandas as pd
import numpy as np
import sys
from numpy.ma.extras import average
from pyecharts.charts import Map, Timeline

import json
import os
from pyecharts import options as opts
#加载地图配置
from pyecharts.globals import CurrentConfig  # 加载全局配置
CurrentConfig.ONLINE_HOST = "http://127.0.0.1:8000/assets/"  # 设定静态资源地址
from pyecharts.datasets import register_url  # 部分地图文件注册
# 注册本地服务器的地图数据源
register_url("http://127.0.0.1:8000/")

data = pd.read_csv('./data/湖南湖北.xlsx')
data['province'] = data['province'].transform(lambda x:x+'省')
data['day'] = pd.to_datetime(data['发货时间']).dt.day

dp = data.groupby(['province','day']).size().reset_index()
dicts = {}
for i in range(1,32):
    dicts[f'第{i}天'] = dp[dp['day'] == i][['province', 0]].values.tolist()
from pyecharts.charts import Timeline
filenames = os.listdir('./data/maps/')
hbhn = {'type': 'FeatureCollection','features':[]}
for i in filenames:
    with open(f"./data/maps/{i}",'r',encoding='utf-8') as f:
        data = json.loads(f.read())
        hbhn['features'].append(data)
target_data = """{
        "type": "FeatureCollection",
        "features": []}"""
target_data = json.loads(target_data)
list_region = os.listdir('./data/maps/')
name_list = []
for lr in list_region:
    with open(f"./data/maps/{lr}", 'r', encoding='utf-8') as f:
        temp = json.load(f)
        temp = temp['features']
        for tp in temp:
            name = tp['properties']['name']
            # 将area加入tp节点并传入target_data
            tp['properties']['area'] = '湖北湖南'
            target_data['features'].append(tp)
            name_list.append((name, np.random.randint(100, 5000)))

t1 = Timeline()
for i in range(1,32):
    maps = Map(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px'))
    maps.add_js_funcs(f"echarts.registerMap('湖北湖南', {target_data});")
    # 引用添加的地图
    maps.add("订单数量",dicts[f'第{i}天'],maptype='湖北湖南')
    maps.set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=800,min_=1))
    t1.add(maps,f'第{i}天')
t1.add_schema(play_interval=300)
t1.render('./映射.html')