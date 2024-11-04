#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :cat_ver_ana.py
# @Time      :2024/10/28 17:28
# @Author    :雨霓同学
# @Function  :
import pandas as pd
from pyecharts.charts import Pie
from pyecharts.globals import ThemeType
from pyecharts import options as opts
from pyecharts.globals import CurrentConfig
from pyecharts.datasets import register_url
from pyecharts.charts import Tab
import styles
import con_var_ana as cva

CurrentConfig.ONLINE_HOST = "http://127.0.0.1:8000/assets/"
register_url("http://127.0.0.1:8000/")
dicts = {'MON': '赊销', 'WDS': '物流代收款', 'YDS': '业务代收款', 'EAX': '款到发货', 'TZZ': '转账支付'}
data = pd.read_csv('./data/两省离散变量.csv', encoding='utf-8')
data['结算方式'] = data['结算方式'].map(dicts)

# 分析湖南,湖北物流结算方式的差异
def get_data(datas, data_source='结算方式'):
    hb = data.groupby(['provience', data_source]).size().loc['湖北'].reset_index()
    hn = data.groupby(['provience', data_source]).size().loc['湖南'].reset_index()
    dt = pd.merge(hb, hn, on=data_source, how='outer')
    dt.fillna(0, inplace=True)
    dt.columns = [data_source, '湖北', '湖南']
    dt.set_index(data_source, inplace=True)
    return dt

def draw_pie(data_pair, title='湖南湖北对比饼图'):
    pie = (Pie(init_opts=opts.InitOpts(theme=ThemeType.CHALK, width='1200px', height='600px'))
        .add("湖北",
            sorted(data_pair['湖北'].reset_index().values.tolist(), key=lambda x: x[1], reverse=True)[:7],
            radius=["25%", "45%"], center=["25%", "50%"],
            itemstyle_opts=styles.pie_style
            )
        .add("湖南",
            sorted(data_pair['湖南'].reset_index().values.tolist(), key=lambda x: x[1], reverse=True)[:7],
            radius=["25%", "45%"], center=["75%", "50%"],
            itemstyle_opts=styles.pie_style
            )
        .set_global_opts(title_opts=[
                dict(text='湖南', top='47%', left='23%'),
                dict(text='湖北', top='47%', left='73%'),
                dict(text=title, left='center')
            ],
            legend_opts=opts.LegendOpts(pos_top="5%", textstyle_opts={'color': 'white', "fontWeight": 'bold'}),
                        )
        .set_series_opts(label_opts=opts.LabelOpts(formatter='{b}:{c}\n\n占比:{d}%',
                        font_weight='bold', color='auto'
                        ))
        )
    return pie


if __name__ == "__main__":

    run_code = 0
    data_dict = get_data(datas=data, data_source='物流录入的结算方法')
    cva.draw_bar(data_dict, title='两省物流录入结算方法对比分析').render()
    draw_pie(data_dict, '湖南湖北物流结算方式对比').render()
    tab = Tab()
    for i in data.columns.tolist()[:-2]:
        data_pair = get_data(datas=data, data_source=i)
        item = draw_pie(data_pair, f'湖南湖北{i}对比')
        tab.add(item, i)
    tab.render('./all_cat.html')

