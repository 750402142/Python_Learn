# 不同的参数组合对决策边界的影响什么

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import matplotx
import numpy as np
from matplotlib import patches
from matplotlib.colors import ListedColormap
from sklearn.datasets import load_iris
from sklearn import neighbors
import seaborn as sns

st.set_page_config(page_title='KNN分类算法之参数对于决策边界的影响',page_icon=':smiley',layout='wide')# 设置页面整体更宽
st.title('KNN分类算法之参数对决策边界的影响演示')
rgb = [[255,238,255],
       [219,238,244],
       [228,228,228]]
rgb = np.array(rgb)/255
cmap_light = ListedColormap(rgb)

#数据的导入
iris_dataset = load_iris()
X = pd.DataFrame(iris_dataset['data']).iloc[:,:2]#只取花萼的长度和宽度
y = iris_dataset['target']
h = 0.02# 用来影响预测区域,越小越准确
x1_min,x1_max = X.iloc[:,0].min() - 0.2,X.iloc[:,0].max() + 0.2
x2_min,x2_max = X.iloc[:,1].min() - 0.2,X.iloc[:,1].max() + 0.2
xx1,xx2 = np.meshgrid(np.arange(x1_min,x1_max,h),np.arange(x2_min,x2_max,h))

with st.sidebar:
    x1 = st.slider("请输入花萼的长度", x1_min, x1_max, 5.5)
    x2 = st.slider("请输入花萼的宽度", x2_min, x2_max, 4.0)
    K = st.slider("请输入领居的数量", 1, 10, 3)
    p = st.selectbox("请选择距离度量", [1, 2], index=1)
    run_code = st.button("运行代码")
st.info(f'你输入的是:{x1,x2,K,p}')
x= np.array([x1,x2])

def knn_model(k_neighbors = 3,weights = 'uniform',p=2):
    knn_clf = neighbors.KNeighborsClassifier(k_neighbors,weights=weights,p=p)
    knn_clf.fit(X, y)
    q = np.c_[xx1.ravel(), xx2.ravel()]
    y_predict = knn_clf.predict(q).reshape(xx1.shape)
    return y_predict,k_neighbors,weights,p,knn_clf
# y_predict,k_neighbors,weights,p,knn_clf = knn_model(k_neighbors = K,weights = 'uniform', p=p)
def creat_plot(y_predict,k_neighbors,weights,p):
    plt.style.use(matplotx.styles.pitaya_smoothie['light'])
    plt.rcParams['font.sans-serif'] = 'Times New Roman'
    fig = plt.figure(figsize=(8, 6))
    plt.contourf(xx1, xx2, y_predict, cmap=cmap_light)  # 使用预测结果填充决策区
    plt.contour(xx1, xx2, y_predict, levels=[0, 1, 2], colors=['red', 'green', 'blue'])
    sns.scatterplot(x=X.iloc[:, 0], y=X.iloc[:, 1],
                    hue=iris_dataset['target_names'][y],
                    linewidth=1, edgecolor='white', alpha=0.7
                    )
    plt.title(f"K-NN classifiter k={k_neighbors}, weight={weights},p = {p}")
    plt.xlim(x1_min, x1_max)
    plt.ylim(x2_min, x2_max)
    plt.xlabel(iris_dataset.feature_names[0])
    plt.ylabel(iris_dataset.feature_names[1])
    plt.grid(linestyle='--', linewidth=0.25, color='gray')
    plt.tight_layout()
    plt.axis('equal')
    return fig

def creart_plot_with_neighbor(y_predict_, k_neighbors_, weight_, p_, x_point, dis_):
    plt.rcParams['font.sans-serif'] = 'Times New Roman'
    plt.rcParams['font.size'] = 16
    figs = plt.figure(figsize=(8, 6), dpi=100)
    plt.contourf(xx1, xx2, y_predict_, cmap=cmap_light)  # 使用预测结果填充决策区域
    plt.contour(xx1, xx2, y_predict_,
                levels=[0, 1, 2], colors=['black', 'orange', 'red'],
                linewidths=1,
                )
    sns.scatterplot(x=X.iloc[:, 0], y=X.iloc[:, 1], hue=iris_dataset.target_names[y],
                    linewidth=1, edgecolor='white', alpha=1
                    )
    plt.title(f'K-NN classifier k={k_neighbors_}, weight={weight_}, p={p_}')
    plt.scatter(x_point[0], x_point[1], marker='*', s=100, color='red')
    plt.xlabel(iris_dataset.feature_names[0])
    plt.ylabel(iris_dataset.feature_names[1])
    plt.grid(linestyle='--', linewidth=0.25, color='gray')
    plt.tight_layout()
    plt.axis('equal')
    circle = patches.Circle(x_point, dis_[-1][-1], fill=False)
    ax = plt.gca()
    ax.set_xlim(xx1.min(), xx1.max())
    ax.set_ylim(xx2.min(), xx2.max())
    ax.add_patch(circle)  # 三个领居
    return figs
if run_code:
    y_predict, k_neighbors, weight, p, clf = knn_model(K, weights='uniform', p=p)
    y_predict1, k_neighbors1, weight1, p1, clf1 = knn_model(K, weights='distance', p=p)
    result, result1 = clf.predict(np.array([x1, x2]).reshape(1, -1)), clf1.predict(np.array([x1, x2]).reshape(1, -1))
    # print(clf.predict(np.array([x1, x2])))
    x = np.array([x1, x2])
    dis, index = clf.kneighbors(x.reshape(1, -1))
    dis1, index1 = clf1.kneighbors(x.reshape(1, -1))
    st.success(f'用户输入的花萼长度为: {x1}, 花萼宽度为: {x2}', icon="✅")

    fig = creat_plot(y_predict, k_neighbors, weights=weight, p=p)
    fig2 = creat_plot(y_predict1, k_neighbors1, weights=weight1, p=p1)
    left, right = st.columns(2)
    left.pyplot(fig)
    left.success(f'预测结果为: {iris_dataset.target_names[clf.predict(np.array([x1, x2]).reshape(1, -1))].tolist()[0]}')
    right.pyplot(fig2)
    right.success(f'预测结果为: {iris_dataset.target_names[clf1.predict(np.array([x1, x2]).reshape(1, -1))].tolist()[0]}')
    left, right = st.columns(2)
    fig3 = creart_plot_with_neighbor(y_predict, k_neighbors, weight, p, x, dis)
    fig4 = creart_plot_with_neighbor(y_predict1, k_neighbors1, weight1, p1, x, dis1)
    left.pyplot(fig3)
    left.success(f"在当前范围内: 存在的领居鸢尾花分别为: {iris_dataset.target_names[y][index].tolist()[0]}")
    right.pyplot(fig4)
    right.success(f"在当前范围内: 存在的领居鸢尾花分别为: {iris_dataset.target_names[y][index1].tolist()[0]}")






