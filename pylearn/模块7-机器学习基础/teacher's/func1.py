#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :func1.py
# @Time      :2024/11/14 10:30
# @Author    :雨霓同学
# @Function  :

import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objs as go
import plotly.io as pio

# 定义两个函数
def f1(x):
    return 2* x ** 2 - 4 * x + 5

def f2(x):
    return x * np.sin(x)
x = np.linspace(-7, 7, 2000)

# 计算两个函数的值
y1 = f1(x)
y2 = f2(x)

# 创建一个线图
fig = go.Figure()
# 添加第一个函数的线
fig.add_trace(go.Scatter(x=x, y=y1, mode='lines', name=r'f1(x) = 2x^2 - 4x + 5'))
# 更新布局以添加标题和图例
fig.update_layout(
    font= dict(family="Times New Roman"),
    title='$f1(x) = 2x^2 - 4x + 5$',
    xaxis=dict(
        title=r'权重 $w$',
        range=[-6, 6],
        linecolor='gray',
        showgrid=False,
        gridcolor='lightgray'  # 设置网格线颜色为浅灰色
    ),
    yaxis=dict(
        linecolor='gray',
        title=r'$\text{损失} Loss$',
        range=[-1,50],
        showgrid=False,
        gridcolor='lightgray'  # 设置网格线颜色为浅灰色
    ),
    legend_title='Functions',
    width=1000,  # 设置画布宽度为800像素x
    height=800,  # 设置画布高度为600像素
    paper_bgcolor='rgba(0,0,0,0)',  # 设置页面背景为透明
    plot_bgcolor='rgba(0,0,0,0)',  # 设置绘图区域背景为透明
    hoverlabel=dict(
        bgcolor='rgba(0,0,0,1)',  # 背景颜色
        bordercolor='rgba(0,0,0,1)',   # 边框颜色
        font=dict(
            family='Times New Roman',   # 字体类型
            size=16,          # 字体大小
            color='cyan'      # 字体颜色
        ),
    )
)

# 显示图表
fig.show()
if __name__ == "__main__":
    run_code = 0
