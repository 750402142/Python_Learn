#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :func2.py
# @Time      :2024/11/14 10:31
# @Author    :雨霓同学
# @Function  :

import plotly.graph_objs as go
from plotly import tools
import numpy as np

# 定义一个三维函数
def f(x, y):
    return 2 * x**2 - 2*x  + y**2 - 3 *y + 3

# 创建x和y的值范围
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# 计算Z的值
Z = f(X, Y)

# 创建三维图形的trace
trace = go.Surface(z=Z, x=X, y=Y, opacity=.7,showscale=False,colorscale="Rainbow",
                  contours = {
#         "z": {"show": True, "start": 0, "end": 50, "size": 5}
    },
                  )

# 创建图形的布局
layout = go.Layout(
    margin=dict(l=0, r=0, b=0, t=0),
    scene=dict(xaxis=dict(nticks=20,
                         title='X',
                         ),
               yaxis=dict(nticks=20,
                         title='Y'
                         ),
               zaxis=dict(nticks=20,
                         title='Loss'
                         ),
               aspectratio=dict(x=1, y=1, z=.8)  # 设置场景的宽高比为等轴
              ),
    font= dict(family="Times New Roman"),
    width=900,  # 设置画布宽度为800像素x
    height=700,  # 设置画布高度为600像素
    paper_bgcolor='rgba(0,0,0,0)',  # 设置页面背景为透明
    plot_bgcolor='rgba(0,0,0,0)',  # 设置绘图区域背景为透明
    hoverlabel=dict(
        bgcolor='rgba(0,0,0,0)',  # 背景颜色
        bordercolor='rgba(0,0,0,0)',   # 边框颜色
        font=dict(
            family='Times New Roman',   # 字体类型
            size=16,          # 字体大小
            color='cyan'      # 字体颜色
        ),
    )
)

# 创建完整的图形
fig = go.Figure(data=[trace], layout=layout)
# fig.update_traces(contours_z=dict(show=True, usecolormap=True,
#                                   highlightcolor="red", project_z=True))
fig.update_layout(
    xaxis=dict(showgrid=True, zeroline=True),
    yaxis=dict(showgrid=True, zeroline=True)
)

# 使用Plotly的orca工具来实现交互式
fig.show()
if __name__ == "__main__":
    run_code = 0
