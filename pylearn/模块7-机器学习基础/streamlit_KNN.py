import pandas as pd
import streamlit as st
import pickle
import folium
from matplotlib import patches
from streamlit_folium import st_folium
from streamlit.components.v1 import html
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotx
import sys
st.set_page_config(layout='wide')# 设置页面整体更宽
plt.style.use(matplotx.styles.pitaya_smoothie['light'])
plt.rcParams['font.sans-serif'] = 'Times New Roman'
raw_data_x = [[3.3935, 2.3313],
[3.1101, 1.7815],
[1.3438, 3.3684],
[3.5823, 4.6792],
[2.2804, 2.8670],
[7.4234, 4.6965],
[5.7451, 3.5340],
[9.1722, 2.5111],
[7.7928, 3.4241],
[7.9398, 0.7916]]
raw_data_y = [0,0,0,0,0,1,1,1,1,1]
data = pd.DataFrame(raw_data_x)
data['y'] = raw_data_y
data.columns = ['x1','x2','y']
st.markdown("# KNN算法演示")
with st.sidebar:
    x1= st.slider('请输入x的第一个坐标',0,10,3)
    x2=st.slider('请输入x的第二个坐标',0.0,5.0,2.5)
    K = st.slider('请输入邻居的数量',0,10,3)
st.info(f'你输入的坐标是:{x1,x2}')
x= np.array([x1,x2])

def draw_sca(data,x):
    fig = plt.figure(figsize=(6, 4), dpi=100)
    plt.scatter(data[data['y'] == 0]['x1'], data[data['y'] == 0]['x2'], s=30, label='蓝色:0')
    plt.scatter(data[data['y'] == 1]['x1'], data[data['y'] == 1]['x2'], s=30, label='红色:0')
    #plt.annotate('x点', xy=(x[0], x[1]), xytext=(6, 2), arrowprops=dict(facecolor='black', shrink=0.05, lw=1))
    plt.scatter(x[0], x[1], marker='*', s=100)
    plt.legend(prop={"family":"STsong"})
    plt.ylim(0, 5)
    plt.title("原始数据的分布",fontproperties='STsong')
    ax = plt.gca()
    ax.set_aspect('equal')
    return fig

def KNN_classfify(K,data,x):
    x = np.array(x)
    dis = ((data[['x1','x2']] - x) ** 2).sum(axis=1).apply(lambda x:np.sqrt(x)).sort_values()
    index = dis.index[:K]
    result = data.iloc[index]['y'].value_counts().to_dict()
    # 方法中的参数key是必需的，它是你想要在字典中查找的键。default参数是可选的，它用于指定当键不存在于字典中时返回的值。
    return f"有{result.get(0,1)},{result.get(1,1)}",dis,index,result

def creat_plot_with_neighbor(data,x,neighboor,index,dis):
    fig = plt.figure(figsize=(7,7),dpi=100)
    plt.scatter(data[data['y'] == 0]['x1'], data[data['y'] == 0]['x2'], s=30, label='蓝色:0')
    plt.scatter(data[data['y'] == 1]['x1'], data[data['y'] == 1]['x2'], s=30, label='红色:0')
    # plt.annotate('x点', xy=(x[0], x[1]), xytext=(6, 2), arrowprops=dict(facecolor='black', shrink=0.05, lw=1))
    plt.scatter(x[0], x[1], marker='*', s=100)
    plt.title(f"当前的邻居数量为:{neighboor}个",fontproperties='STsong')

    circle = patches.Circle(x,dis[index[neighboor -1]],fill=False)
    ax = plt.gca()
    ax.add_patch(circle)
    ax.set_aspect('equal')
    plt.legend(prop = {'family':"STsong"})
    plt.ylim(0, 5)
    return fig
info,dis,index,result = KNN_classfify(K,data,x)
left,right = st.columns(2)
left.pyplot(draw_sca(data,x))
right.pyplot(creat_plot_with_neighbor(data,x,K,index,dis))
st.success(info)

if result.get(0,0) > result.get(1,0):
    st.info('目标点预测结果为: 0')
elif result.get(1,0) > result.get(0,0):
    st.info('目标点预测结果为: 1')
else:
    st.info('目标点邻居数量一致,建议更换邻居的数量,设为奇数个')
