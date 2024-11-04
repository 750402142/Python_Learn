#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :con_var_ana.py
# @Time      :2024/10/28 08:12
# @Author    :雨霓同学
# @Function  :

import pandas as pd
from pyecharts.charts import Line
from pyecharts.charts import Tab
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType
from pyecharts import options as opts
from pyecharts.globals import CurrentConfig
from pyecharts.datasets import register_url
import matplotlib.pyplot as plt
import matplotx
import styles

CurrentConfig.ONLINE_HOST = "http://127.0.0.1:8000/assets/"
register_url("http://127.0.0.1:8000/")


def get_data(filepath, data_source='发货金额', action_name='sum', ):
    """
    根据指定的文件路径、省份名称、数据源和操作类型，从CSV文件中获取并处理数据。

    参数:
    - filepath: CSV文件的路径。
    - data_source: 数据源列的名称，默认为'发货金额'。
    - action_name: 对数据源列执行的操作，默认为求和'。

    返回:
    - 包含指定省份时间和数据源操作结果的DataFrame。
    """
    # 读取CSV文件并转换时间格式
    data = pd.read_csv(filepath_or_buffer=filepath, encoding='utf-8')
    data['time'] = pd.to_datetime(data['time'])
    data.sort_values(by=['time'], inplace=True)
    data['time'] = data['time'].apply(lambda x: x.strftime('%m-%d'))

    # 根据省份和时间对数据进行分组，并执行指定的操作
    data_p = data.groupby(['provience', 'time'])[data_source].agg(action_name).astype('int').reset_index()

    # 获取指定省份的数据并返回
    data_hn = data_p[data_p['provience'] == '湖北'][['time', data_source]]
    data_hb = data_p[data_p['provience'] == '湖南'][['time', data_source]]
    return data_hn, data_hb

def get_sum_data(column_list):
    data = pd.read_csv('./data/两省连续变量.csv')
    data_pa = data.groupby('provience')[column_list].sum().T
    return data_pa
def draw_line(data_dict, title, area=True):
    """
    绘制折线图。
    参数:
    - data_dict: 字典类型，包含要绘制的折线图的数据，key为折线图的名称，value为包含x轴和y轴数据的DataFrame。
    - title: 字符串类型，折线图的标题。
    返回:
    - line: 返回一个绘制好的折线图对象。
    """
    # 初始化折线图，设置主题、宽度和高度
    line = Line(init_opts=opts.InitOpts(theme=ThemeType.CHALK))
    # 添加x轴数据，这里假设所有数据的x轴是相同的
    line.add_xaxis(list(data_dict.values())[0].iloc[:, 0].tolist())
    # 遍历字典，为每组数据添加折线图
    for index, item in enumerate(data_dict.items()):
        line.add_yaxis(
            item[0],
            item[1].iloc[:, -1].tolist(),
            is_smooth=True,
            is_symbol_show=False,
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=styles.line_style
        )
        if area:
            area_style = styles.get_area_style_color()
            line.options['series'][index]['areaStyle'] = area_style
        else:
            line.options['series'][index]['areaStyle'] = opts.AreaStyleOpts(opacity=0)

    # 设置全局配置项
    line.set_global_opts(
        title_opts=opts.TitleOpts(title=title),  # 设置标题
        tooltip_opts=opts.TooltipOpts(is_show=True, trigger='axis', axis_pointer_type='cross'),
        datazoom_opts=[opts.DataZoomOpts(type_='inside')],  # 设置数据区域缩放
        # 配置x轴
        xaxis_opts=opts.AxisOpts(
            splitline_opts={"show": False},
            axislabel_opts=opts.LabelOpts(color='white', font_weight='bold'),  # 设置标签样式
            axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(color='white')),
        ),
        # 配置y轴
        yaxis_opts=opts.AxisOpts(
            splitline_opts={"show": True},
            axislabel_opts=opts.LabelOpts(color='white', font_weight='bold'),
            axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(color='white')),
        ),
        # 设置图例样式
        legend_opts=opts.LegendOpts(textstyle_opts=opts.TextStyleOpts(font_weight='bold', color='auto'))
    )

    # 设置系列配置项
    line.set_series_opts(
        label_opts=opts.LabelOpts(is_show=False),
    )

    return line

def draw_tab(chart_dict):
    """
    创建一个包含多个图表的标签页。

    :param chart_dict: 字典，键为图表对象，值为标签名称
    :return: 包含多个图表的标签页对象
    """
    if not chart_dict:
        raise ValueError("至少存在一个图表")

    try:
        tab = Tab()
        for chart, name in chart_dict.items():
            tab.add(name, chart)
    except Exception as e:
        # 处理可能的异常
        print(f"Error adding charts to tab: {e}")
        raise

    return tab

def draw_bar(data,title='两个省份其他字段分析', rotate=0):
    bar_chart = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.CHALK,
                                    ))
        .add_xaxis(data.index.tolist())
        .add_yaxis('湖北', [int(x) for x in data['湖北'].tolist()],
                bar_max_width='60%',
                category_gap=0,
                gap=0,
                # itemstyle_opts=styles.get_area_style_color()
                )
        .add_yaxis('湖南', [int(x) for x in data['湖南'].tolist()],
                bar_max_width='60%',
                gap=0,
                # itemstyle_opts=styles.get_area_style_color()
                )
        .set_global_opts(
            title_opts=opts.TitleOpts(title=title),
            legend_opts=opts.LegendOpts(
                is_show=True, textstyle_opts=opts.TextStyleOpts(color='auto')),
            tooltip_opts=opts.TooltipOpts(
                is_show=True, trigger='axis', axis_pointer_type='shadow'),
            xaxis_opts=opts.AxisOpts(
                splitline_opts={"show": False},
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color='white')),
                axislabel_opts=opts.LabelOpts(color='white', font_weight='bold', rotate=rotate),
            ),
            yaxis_opts=opts.AxisOpts(
                splitline_opts={"show": True},
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color='white')),
                axislabel_opts=opts.LabelOpts(color='white', font_weight='bold'),
            ),
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=True,
                font_weight='bold', position='top'
                                        ))
    )

    return bar_chart

def get_matplotlib_scatter():
    """
    主要是用于完成: 发货体积,发货净重,发货数量两省 分布分析

    :return:
    """
    data = pd.read_csv('./data/两省连续变量.csv')
    from sklearn.preprocessing import MinMaxScaler
    data['发货数量'] = data['发货小包装数量'] + data['发货大包装数量']
    data_hn = data[data['provience'] == '湖南'].copy()
    data_hb = data[data['provience'] == '湖北'].copy()
    scaler = MinMaxScaler()
    data_hb[['发货毛重', '发货体积',
            '发货数量']] = scaler.fit_transform(data_hb[['发货毛重', '发货体积', '发货数量']])
    data_hn[['发货毛重', '发货体积',
            '发货数量']] = scaler.fit_transform(data_hn[['发货毛重', '发货体积', '发货数量']])
    plt.rcParams['font.sans-serif'] = 'STsong'
    plt.rcParams['font.size'] = 16
    plt.style.use(matplotx.styles.pitaya_smoothie['light'])
    fig = plt.figure(figsize=(10, 6), dpi=100)
    plt.scatter(data_hn['发货数量'], data_hn['发货毛重'], s=data_hn['发货体积'] * 400,
                color='blue', marker='o', label='湖南', alpha=0.7, edgecolors='white', lw=0.5)
    plt.scatter(data_hb['发货数量'], data_hb['发货毛重'], s=data_hb['发货体积'] * 400,
                color='red', marker='o', label='湖北', alpha=0.7, edgecolors='white', lw=0.5
                )
    plt.xlabel('发货数量')
    plt.ylabel('发货毛重')
    plt.title('湖南湖北两地物流数量,毛重,体积关系分布', fontsize=20)
    plt.legend()
    # plt.savefig('./results/fig.png', dpi=400, bbox_inches='tight', pad_inches=0.0)
    return fig

data_s, data_n = get_data(filepath='./data/两省连续变量.csv', data_source='发货金额', action_name='sum')
data_s1, data_n1 = get_data(filepath='./data/两省连续变量.csv', data_source='折扣金额', action_name='sum')
data_s2, data_n2 = get_data(filepath='./data/两省连续变量.csv', data_source='代垫费用应收金额', action_name='sum')
line1 = draw_line(
    {'湖南发货金额': data_s, '湖北发货金额': data_n,
    '湖南折扣金额': data_s1, '湖北折扣金额': data_n1,
    '湖南代垫费用应收金额': data_s2, '湖北代垫费用应收金额': data_n2,
    }, title='两个省份金额类字段时序分析折线线图', area=True)

print(line1.render_embed())
if __name__ == "__main__":
    # data_s, data_n = get_data(filepath='./data/两省连续变量.csv', data_source='发货金额', action_name='sum')
    # data_s1, data_n1 = get_data(filepath='./data/两省连续变量.csv', data_source='折扣金额', action_name='sum')
    # data_s2, data_n2 = get_data(filepath='./data/两省连续变量.csv', data_source='代垫费用应收金额', action_name='sum')
    # line1 = draw_line(
    #     {'湖南发货金额': data_s, '湖北发货金额': data_n,
    #     '湖南折扣金额': data_s1, '湖北折扣金额': data_n1,
    #     '湖南代垫费用应收金额': data_s2, '湖北代垫费用应收金额': data_n2,
    #     }, title='两个省份金额类字段时序分析折线线图', area=True).render()
    # columns = ['发货小包装数量', '发货毛重', '发货体积', '打印次数',
    #         'WMS系统实际拣货数量', '发货单WMS系统锁定库存优先级',
    #         '发货大包装数量', 'WMS系统实际拣货数量', ]
    # data_pair = get_sum_data(columns)
    # bar = draw_bar(data_pair)
    # bar.render()
    # print(data_pair)
    # bar.render()
    """
    发货折扣: 折线图
    发货金额: 折线图
    发货折扣+发货金额: Tab组件
    其他字段分析: Bar
    货物状态分布分析: Scatter
    """
    get_matplotlib_scatter()


