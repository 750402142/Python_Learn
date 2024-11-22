#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :NCC_demo.py
# @Time      :2024/11/13 09:25
# @Author    :雨霓同学
# @Function  :
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets
from matplotlib.colors import ListedColormap
from sklearn.neighbors import NearestCentroid  # 最近质心分类

st.set_page_config(page_title="NCC分类算法之参数对决策边界的影响演示", page_icon=":smiley:", layout="wide")
st.title("NCC分类算法之参数对决策边界的影响演示")

rgb = [[255, 238, 255],  # 红
       [219, 238, 244],  # 蓝
       [228, 228, 228]]  # 黑
rgb = np.array(rgb) / 255
cmap_light = ListedColormap(rgb)

iris = datasets.load_iris()  # 导入鸢尾花数据集
X = iris.data[:, :2]  # 只使用前两个特征,花萼的长度和宽度
y = iris.target  # 提取数据的标签
# 创建网格
h = 0.02  # 网格当中的步长
x1_min, x1_max = X[:, 0].min() - 0.2, X[:, 0].max() + 0.2
x2_min, x2_max = X[:, 1].min() - 0.2, X[:, 1].max() + 0.2
#  创建网格点矩阵
xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, h),
                       np.arange(x2_min, x2_max, h)
                       )


def ncc_model(metric_, shrink_threshold_=None):
    clf_nc_ = NearestCentroid(metric='euclidean', shrink_threshold=shrink_threshold_)
    clf_nc_.fit(X, y)
    y_pred = clf_nc_.predict(np.c_[xx1.ravel(), xx2.ravel()])
    y_pred = y_pred.reshape(xx1.shape)
    return y_pred, metric_, shrink_threshold_, clf_nc_


def creat_plot(y_predict_, metrics_, shrink_threshold_, clf_nc_):
    plt.rcParams['font.sans-serif'] = 'Times New Roman'
    plt.rcParams['font.size'] = 16
    figs = plt.figure(figsize=(8, 6), dpi=100)
    plt.contourf(xx1, xx2, y_predict_, cmap=cmap_light)  # 使用预测结果填充决策区域
    plt.contour(xx1, xx2, y_predict_,
                levels=[0, 1, 2], colors=['black', 'orange', 'red'],
                linewidths=1,
                )
    center = clf_nc_.centroids_
    sns.scatterplot(x=center[:, 0], y=center[:, 1], color='red', marker='*', s=420, label='Centroid', )
    sns.scatterplot(x=X[:, 0], y=X[:, 1], hue=iris.target_names[y],
                    linewidth=1, edgecolor='white', alpha=1,
                    )
    plt.title(f'NCC classifier metric={metrics_}, shrink_threshold={shrink_threshold_}')
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())
    plt.xlabel(iris.feature_names[0])
    plt.ylabel(iris.feature_names[1])
    # plt.legend()
    plt.grid(linestyle='--', linewidth=0.25, color='gray')
    plt.tight_layout()
    ax = plt.gca()
    ax.set_aspect('equal')
    return figs


def get_dis(clf_nc_, x1_=5.0, x2_=3.0):
    centroids = clf_nc_.centroids_
    # 要计算待预测点与每个质心的距离
    X_new = np.array([[x1_, x2_]])
    # 计算距离
    distances = np.linalg.norm(centroids - X_new, axis=1)
    # 确定属于哪个类别
    predicted_class = np.argmin(distances)
    return distances, iris.target_names[predicted_class]


def creat_bar(datax_):
    fig_ = plt.figure(figsize=(8, 5), dpi=100)
    plt.bar(iris.target_names, datax_, width=0.4, color='orange', edgecolor='black', linewidth=1)
    for x_, y_ in zip(iris.target_names, datax_):
        plt.text(x_, y_ + 0.05, f"{y_:.2f}cm", va='center', ha='center')
    plt.xlabel('iris_target')
    plt.ylabel('distance')
    # 获取当前的 Axes 对象
    ax = plt.gca()

    # 关闭上面和右边的轴线
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    return fig_


with st.sidebar:
    x1 = st.slider("请输入花萼的长度", x1_min, x1_max, 5.5)
    x2 = st.slider("请输入花萼的宽度", x2_min, x2_max, 4.0)
    shrink_threshold = st.selectbox("请输入收缩阈值", [None, 0.5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    metrics = st.selectbox("请选择距离度量", ['euclidean', 'manhattan', 'cosine'], index=1)

y_predict, metric, shrink_threshold, clf_nc = ncc_model(metric_='euclidean', shrink_threshold_=shrink_threshold)
y_predict1, metric1, shrink_threshold1, clf_nc1 = ncc_model(metric_=metrics, shrink_threshold_=shrink_threshold)
result, result1 = clf_nc.predict(np.array([x1, x2]).reshape(1, -1)), clf_nc.predict(np.array([x1, x2]).reshape(1, -1))

x = np.array([x1, x2])

st.success(f'用户输入的花萼长度为: {x1}, 花萼宽度为: {x2}', icon="✅")

fig = creat_plot(y_predict, metric, shrink_threshold, clf_nc_=clf_nc)
fig2 = creat_plot(y_predict1, metric1, shrink_threshold1, clf_nc_=clf_nc1)

datax, label = get_dis(clf_nc, x1_=x1, x2_=x2)
datax1, label1 = get_dis(clf_nc1, x1_=x1, x2_=x2)

left, right = st.columns(2)
left.pyplot(fig)
left.success(f'预测结果为: {iris.target_names[clf_nc.predict(np.array([x1, x2]).reshape(1, -1))].tolist()[0]}')
right.pyplot(fig2)
right.success(f'预测结果为: {iris.target_names[clf_nc.predict(np.array([x1, x2]).reshape(1, -1))].tolist()[0]}')

left, right = st.columns(2)
fig3, fig4 = creat_bar(datax), creat_bar(datax1)
left.pyplot(fig3)
left.success(f"在当前范围内,最短距离为: {datax.min():.2f} cm")
right.pyplot(fig4)
right.success(f"在当前范围内, 最短距离为: {datax1.min():.2f} cm")

if __name__ == "__main__":
    run_code = 0
