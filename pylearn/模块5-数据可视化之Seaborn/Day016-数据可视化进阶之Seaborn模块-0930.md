# Day016-数据可视化进阶之Seaborn模块-0930


```python
import seaborn as sns #  pip install seaborn==0.13.2
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sys
print(f"Seaborn版本{sns.__version__}")
print('Python version:', sys.version)
print('Pandas version:', pd.__version__)
print('Numpy version:', np.__version__)
print('Matplotlib version:', matplotlib.__version__)
```

    Seaborn版本0.13.2
    Python version: 3.12.3 | packaged by conda-forge | (main, Apr 15 2024, 18:20:11) [MSC v.1938 64 bit (AMD64)]
    Pandas version: 2.2.2
    Numpy version: 1.26.4
    Matplotlib version: 3.8.4


## Seaborn的基本使用


```python
tips = pd.read_csv('./data/tips.csv')
# print(tips.head().to_markdown())
```

|    |   消费金额 (\$) |   小费金额 (\$) | 客人性别   | 是否吸烟   | 周几   | 就餐时间   |   一起就餐人数 (个) |
|---:|---------------:|---------------:|:-----------|:-----------|:-------|:-----------|--------------------:|
|  0 |          16.99 |           1.01 | Female     | No         | Sun    | Dinner     |                   2 |
|  1 |          10.34 |           1.66 | Male       | No         | Sun    | Dinner     |                   3 |
|  2 |          21.01 |           3.5  | Male       | No         | Sun    | Dinner     |                   3 |
|  3 |          23.68 |           3.31 | Male       | No         | Sun    | Dinner     |                   2 |
|  4 |          24.59 |           3.61 | Female     | No         | Sun    | Dinner     |                   4 |


```python
plt.rcParams['font.sans-serif'] = 'STsong'
import matplotx
with plt.style.context(matplotx.styles.pitaya_smoothie['light']):
    sns.relplot(
        data = tips,     # 指定数据集
        x='小费金额 ($)', # 指定x轴变量
        y='消费金额 ($)', # 指定y轴变量
        col='就餐时间',   # 设置就餐时间为种类,按照分面仅限绘图
        hue='是否吸烟',  # 散点颜色按照是否吸烟而变化,
        style='客人性别', # 散点的种类按照 客人性别变化
        s = 100,
    )
plt.savefig('./image/seaborn_01.png',dpi=300)
```


![png](output_5_0.png)
    


## seaborn中的两类绘图函数
1. figure-level(图形级别的):类似与在matplotlib中使用plt.figure创建一个包含多个子图的画布,他们管理一个整体的图形对象.主要是用于管理多个子图对象.
2. axes-level(坐标轴级别): 可以针对某个特定的子图进行高度的定制化,类似于你在matplotlib中使用ax对象进行绘图.可以精确的空值图形的各个细节.

### figure-level(图形级别的)


```python
penguins = pd.read_csv('./data/penguins.csv')
plt.rcParams['font.size'] = 16
sns.displot(
    data = penguins,
    x =  '喙长 (毫米)',
    hue = '企鹅的种类',
    col = '企鹅的种类',
    palette=['cyan','red','orange'],
    binwidth=1, # 缺点很明显,很多时候不能对子图做定制化
    height=5, # 通过height调整图形的高度
    aspect=1# 通过height * aspect设置图形的宽度
)   
```




    <seaborn.axisgrid.FacetGrid at 0x255e56cc1d0>




​    
![png](output_8_1.png)
​    



```python
penguins.columns
```




    Index(['企鹅的种类', '岛屿', '喙长 (毫米)', '喙深 (毫米)', '鳍长 (毫米)', '体重', '性别'], dtype='object')



### axes-level多子图个性化


```python
fig,axs = plt.subplots(1,2,figsize=(15,5),dpi=100,
                    gridspec_kw=dict(width_ratios=[4,2])
                      )

sns.scatterplot( # 绘制是散点图
    data=penguins,
    x =  '喙深 (毫米)',
    y =  '喙长 (毫米)',
    hue = '企鹅的种类',
    ax = axs[0]
)

sns.histplot( # 绘制直方图
    data = penguins,
    x = '企鹅的种类', 
    hue = '企鹅的种类',
    shrink=0.5,
    ax=axs[1]
)
```




    <Axes: xlabel='企鹅的种类', ylabel='Count'>




​    
![png](output_11_1.png)
​    


## 相关关系图-relational plots


```python
tips = pd.read_csv('./data/tips.csv')

sns.relplot(data=tips,                # 用于绘图的数据集,必选参数
           x = '消费金额 ($)',         #  指定x轴的变量名称,
           y = '小费金额 ($)',         #  指定y轴的变量名称,
           color = 'red',             # 如果是散点图,设定的点的颜色
          hue = '客人性别',            #  用于确认不同数据集的变量名称,通常用不同的颜色表示
#            s=100,                  # 设置点的大小
           kind='scatter',             # 指定图表的类型
           col='是否吸烟',              # 用于在不同的列上创建子图的变量
           col_order=['Yes','No'],    # 对于不同的列上的数据做排序
           row = '就餐时间',                     # 用于在不同的行上指定创建变量
           row_order=['Lunch','Dinner'],       # 对于不同的行上的数据做排序 
           size='一起就餐人数 (个)',             # 点的大小来表示就就餐人数的多少,
           sizes=(1,300),                     # 设置点波动的范围.
           palette=['red','blue'],            # 设置点的颜色,
           )
```




    <seaborn.axisgrid.FacetGrid at 0x255ee227c50>




​    
![png](output_13_1.png)
​    



```python
tips.columns
```




    Index(['消费金额 ($)', '小费金额 ($)', '客人性别', '是否吸烟', '周几', '就餐时间', '一起就餐人数 (个)'], dtype='object')




```python
sns.relplot(data=tips,                # 用于绘图的数据集,必选参数
           x = '消费金额 ($)',         #  指定x轴的变量名称,
           y = '小费金额 ($)',         #  指定y轴的变量名称,
           hue = '客人性别',           #  用于确认不同数据集的变量名称,通常用不同的颜色表示
           col='一起就餐人数 (个)',     # 
           col_wrap=3,               # 设定每行显示的个数
           )
```




    <seaborn.axisgrid.FacetGrid at 0x255f9332330>




​    
![png](output_15_1.png)
​    


## 直方图
- displot(kind='hist'): figure-level
- hisplot: axes-level


```python
penguins.columns
```




    Index(['企鹅的种类', '岛屿', '喙长 (毫米)', '喙深 (毫米)', '鳍长 (毫米)', '体重', '性别'], dtype='object')




```python
sns.displot(
    data = penguins,
    x = '企鹅的种类',                   # 设定X轴的变量, 鳍长 (毫米)
#     y =  '鳍长 (毫米)',                # 设定y轴变量,如果是直方图则建议只设置一个xor y, 会修改显示的方向
    kind='hist',                        # 设定图表的类型为hist
    bins = 10,                   # 设定分箱子的数量,可以指定数目,也可以设定短点[160,180,200,220,240]
    discrete = True,           #  相当于条形图,适用于离散数据
    binwidth=1,            # 设置柱子的宽度,
    shrink = .5,           # 设置柱子区间的相对宽度,柱子之间太过拥挤时使用
    fill=False,           # 关闭填充
)
```




    <seaborn.axisgrid.FacetGrid at 0x255fb3cf200>




​    
![png](output_18_1.png)
​    


### 箱子的呈现方式


```python
items = ['bars','step','poly']
count_style = ['frequency','probability','percent','density'] # 数据统计方式
fig,axs = plt.subplots(1,4,figsize = (20,5),dpi=100)
for i,item in enumerate(count_style):
    sns.histplot(
        data = penguins,
        x = '鳍长 (毫米)',                   # 设定X轴的变量, 鳍长 (毫米)
        bins = 10,                   # 设定分箱子的数量,可以指定数目,也可以设定短点[160,180,200,220,240]
#         element = item,             # 箱子的呈现方式
        stat=item,                  # 数据统计方式
        ax=axs[i]
    )
```


​    
![png](output_20_0.png)
​    


layer: 按照layer进行叠加

stack : 标准的堆积

fill: 百分比堆积

dodge: 分组


```python
sns.displot(
    data = penguins,
    x = '鳍长 (毫米)',                   # 设定X轴的变量, 鳍长 (毫米)
    hue = '企鹅的种类',
    kind='hist',                        # 设定图表的类型为hist
    multiple='dodge'  ,                 # 分组模式
    row = '性别',                       # 行按照性别分组
    col = '岛屿' ,                     # 列按照岛屿分组
    bins = 10,
)
```




    <seaborn.axisgrid.FacetGrid at 0x255972870e0>




​    
![png](output_22_1.png)
​    


### 核密度图KDE

相比与直方图的连续性,KDE提供了数据分布的连续估计.识别数据中的模式,和异常值,


```python
sns.displot(
    data = penguins,
    x = '鳍长 (毫米)',                   # 设定X轴的变量, 鳍长 (毫米),如果设定是y,则图变为水平方向
    hue='岛屿',
    kind='kde',                    # 设定图表的类型为hist
    fill = True,           # 填充密度曲线下的区域
    multiple = 'layer',  # stack是堆叠,layer是叠加,fill是百分比叠加
)
```




    <seaborn.axisgrid.FacetGrid at 0x255a2e5f6e0>




​    
![png](output_24_1.png)
​    


### 核密度图二维模式


```python
sns.displot(
    data = penguins,
    x = '鳍长 (毫米)',                   # 设定X轴的变量, 鳍长 (毫米),如果设定是y,则图变为水平方向
    y = '喙长 (毫米)',            # 指定第二个变量
    kind='kde',                    # 设定图表的类型为hist
    fill = False,            # 设置填充
    levels = 6,             # 设定轮廓线的数量
    thresh=0.06,            # 等值线的最低等比例水平
    hue = '岛屿',            # 分组   
)
```




    <seaborn.axisgrid.FacetGrid at 0x255af331eb0>




​    
![png](output_26_1.png)
​    



```python
sns.displot(
    data = penguins,
    x = '鳍长 (毫米)',                   # 设定X轴的变量, 鳍长 (毫米),如果设定是y,则图变为水平方向
    kind='kde',                    # 设定图表的类型为hist
    fill = True,            # 设置填充
    hue = '企鹅的种类',            # 分组   
    row = '性别',
    col = '岛屿',
)
plt.show()
```


​    
![png](output_27_0.png)
​    


## 分类关系图

- catplot: figure-level函数
- axes-level:
    - boxplot,violinplot,barplot,countplot...

## catplot综合使用


```python
titanic = pd.read_csv('./data/titanic.csv')
# print(titanic.head().to_markdown())
```

|    |   获救情况 |   船票等级 | 性别   |   年龄 |   同乘兄弟姐妹/配偶数量 |   同乘的父母/子女数量 |    票价 | 登船港口   | 船票等级1   | 乘客分类   | 是否成年男性   | 船舱号码   | 登船港口1   | 获救情况1   | 是否独自一人   |
|---:|-----------:|-----------:|:-------|-------:|------------------------:|----------------------:|--------:|:-----------|:------------|:-----------|:---------------|:-----------|:------------|:------------|:---------------|
|  0 |          0 |          3 | male   |     22 |                       1 |                     0 |  7.25   | S          | Third       | man        | True           | nan        | Southampton | no          | False          |
|  1 |          1 |          1 | female |     38 |                       1 |                     0 | 71.2833 | C          | First       | woman      | False          | C          | Cherbourg   | yes         | False          |
|  2 |          1 |          3 | female |     26 |                       0 |                     0 |  7.925  | S          | Third       | woman      | False          | nan        | Southampton | yes         | True           |
|  3 |          1 |          1 | female |     35 |                       1 |                     0 | 53.1    | S          | First       | woman      | False          | C          | Southampton | yes         | False          |
|  4 |          0 |          3 | male   |     35 |                       0 |                     0 |  8.05   | S          | Third       | man        | True           | nan        | Southampton | no          | True           |


```python
plt.rcParams['font.sans-serif'] = 'STsong'
sns.catplot(
    data = titanic,
    y = '年龄',   # 箱子沿着垂直度方向
    kind='box',   # kind指定为箱线图
    width = .3, # 设置箱子的宽度
    fliersize=10,  # 设置异常点的大小
    flierprops = {  # 异常点的个性化设置
        'marker': 'o',  # 设置点的类型
        'markerfacecolor': 'red',
        'alpha':0.3
    },
    showfliers = True, # 不显示异常点
    capprops = {  # 上下边缘线个性化
        'linestyle':'-', # 线条的样式
        'linewidth':2, # 线条灯粗细
        'color':'red'
    },
    showcaps=True, # 通过设置showcaps可以选则关闭上下边缘线
    whiskerprops={  # 须触线的自定义设置
        'linestyle':'dotted', # 线条的样式
        'linewidth':2, # 线条灯粗细
        'color':'red'
    },
    boxprops = { # 箱体内部的填充设置
        'facecolor':'orange',
        'edgecolor':'red',
        'linewidth':2, # 线条灯粗细
    },
    medianprops = {  # 中位数属性个性化
        'linestyle':'-',
        'color':'green',
    },
    showmeans = True, # 显示平均数
    meanprops = { #@ 平均数个性化
        'marker':'o',  # 点的类型
        'markerfacecolor': 'cyan',# 点的颜色
        'markeredgecolor':'black', # 点边缘的颜色
        'markeredgewidth':1, # 点边缘线条灯粗细
        'markersize':10, # 均值点的大小
        'linewidth':2, # 均值线条
        'linestyle': '-'
    },
    meanline=True, # 显示均值线
    notch = True, # 添加置信区间,
    bootstrap=1000, # 通过booststrap随机抽样计算凹口位置
    x = '登船港口',
    hue = '性别',
    order = ['Q','C','S'], 
    palette='Accent'
)
```




    <seaborn.axisgrid.FacetGrid at 0x2530bb78ef0>




​    
![png](output_32_1.png)
​    



```python
plt.rcParams['font.sans-serif'] = 'STsong'
sns.catplot(
    data = titanic,
    y = '年龄',   # 箱子沿着垂直度方向
    kind='box',   # kind指定为箱线图
    x = '登船港口',
    hue = '性别',
    order = ['Q','C','S'], 
    palette="Accent"   # ['red','blue'], 设置颜色
)
```




    <seaborn.axisgrid.FacetGrid at 0x25312be7ad0>




​    
![png](output_33_1.png)
​    



```python
plt.rcParams['font.sans-serif'] = 'STsong'
plt.rcParams['font.size'] = 15
sns.catplot(
    data = titanic,
    y = '年龄',   # 箱子沿着垂直度方向
    kind='box',   # kind指定为箱线图
    x = '登船港口',
    hue = '性别',
    col='船票等级', # 列按照船票等级分面
    row='获救情况',  # 行按照获救情况分面
    order = ['Q','C','S'], 
    palette="Accent"   # ['red','blue'], 设置颜色
)
```




    <seaborn.axisgrid.FacetGrid at 0x25313e12a20>




​    
![png](output_34_1.png)
​    



```python
sns.plotting_context() # 使用context可以定义一些自定义的美化内容
```




    {'font.size': 15.0,
     'axes.labelsize': 'medium',
     'axes.titlesize': 'large',
     'xtick.labelsize': 'medium',
     'ytick.labelsize': 'medium',
     'legend.fontsize': 'medium',
     'legend.title_fontsize': None,
     'axes.linewidth': 0.8,
     'grid.linewidth': 0.8,
     'lines.linewidth': 1.5,
     'lines.markersize': 6.0,
     'patch.linewidth': 1.0,
     'xtick.major.width': 0.8,
     'ytick.major.width': 0.8,
     'xtick.minor.width': 0.6,
     'ytick.minor.width': 0.6,
     'xtick.major.size': 3.5,
     'ytick.major.size': 3.5,
     'xtick.minor.size': 2.0,
     'ytick.minor.size': 2.0}




```python
import seaborn as sns
for item in ['qualitative','diverging','sequentital']:  
    sns.choose_colorbrewer_palette(
        data_type=item, # diverging,'sequentital'
        as_cmap=False
    )
```


    interactive(children=(Dropdown(description='name', options=('Set1', 'Set2', 'Set3', 'Paired', 'Accent', 'Paste…



    interactive(children=(Dropdown(description='name', options=('RdBu', 'RdGy', 'PRGn', 'PiYG', 'BrBG', 'RdYlBu', …



    interactive(children=(Dropdown(description='name', options=('Greys', 'Reds', 'Greens', 'Blues', 'Oranges', 'Pu…


## 相关性热图


```python
data = pd.read_csv('./data/heatmap.csv',header=0,index_col=0)
```


```python
plt.figure(figsize=(10,8),dpi=100)

sns.heatmap(
    data = data.corr(), # 传入相关系数矩阵
    annot=True,  # 是否显示文本标记
    square=True, # 是否显示为正方形
    cmap='RdYlBu_r',
    vmax=1,  # 设定最大值
    vmin=-1, # 设定最小值
)
plt.show()
```


​    
![png](output_39_0.png)
​    


- Pearson相关系数: 
    - 适用于衡量两个连续变量之间的之间的线性个关系
    - 数据应该尽可能满足正太分布
    - 对数据中的离群值比较敏感
- Kendall相关系数
    - 适合非参数统计,特别是数据不满足正太分布时
    - 对数据当中的异常值不敏感
- Spearman相关系数
    - 适合非参数统计,特别是数据不满足正太分布时
    - 对数据当中的异常值不敏感
    - 适用衡量两个变量的单调关系,无论是线性还是非线性都可以


```python
plt.figure(figsize=(10,8),dpi=100)

sns.heatmap(
    data = data.corr(method='pearson'), # 传入相关系数矩阵pearson,spearman,kendall
    annot=True,  # 是否显示文本标记
    square=True, # 是否显示为正方形
    cmap='RdYlBu_r',
    vmax=1,  # 设定最大值
    vmin=-1, # 设定最小值
#     mask=np.triu(np.ones_like(data.corr())) # 绘制下三角形相关矩阵
    mask=np.tril(np.ones_like(data.corr())) # 绘制下三角形相关矩阵
    
)
plt.show()
```


​    
![png](output_41_0.png)
​    


## 组合关系图

用于在单个图表中展示多种图形,以便从不同的维度深入挖掘数据
- pairplot, PairGrid:散点图矩阵
- joingrids, 边际图

### 散点图矩阵

查看数据集中连续型变量之间的关系


```python
data = pd.read_csv('./data/penguins.csv')
```


```python
sns.pairplot(
    data = data,
    plot_kws=dict(color='red',alpha=1), # 非对角线上图的颜色
    diag_kws=dict(color='orange',alpha=1), # 对角线上图的颜色
    height=2, # 调整子图的高度
    aspect=1, # 宽度为height * aspect
    corner=True, # 仅显示下三角形
    hue='性别',  # 按照性别的分类映射不同的颜色
    hue_order=['FEMALE','MALE'], # 分组的颜色顺序
    palette= ['#76c2df','#ef8b7c'], # 颜色可以指定列表['#76c2df','#ef8b7c'],'Set1'#
    markers=['o','s'], # 标记点的样式
#     diag_kind='None', # 不现实对接线上的图b表
    kind='kde', # 设定非对角线图表,可选的kde,hist,scatter
    diag_kind='hist', # 设定对角线上面的图标,一遍显示为 kde和hist
)
```




    <seaborn.axisgrid.PairGrid at 0x25338183290>




​    
![png](output_45_1.png)
​    



```python
g = sns.pairplot(
    data = data,
    plot_kws=dict(color='red',alpha=1), # 非对角线上图的颜色
    diag_kws=dict(color='orange',alpha=1), # 对角线上图的颜色
    height=2, # 调整子图的高度
    aspect=1, # 宽度为height * aspect
    hue='性别',  # 按照性别的分类映射不同的颜色
    hue_order=['FEMALE','MALE'], # 分组的颜色顺序
    palette= ['#76c2df','#ef8b7c'], # 颜色可以指定列表['#76c2df','#ef8b7c'],'Set1'#
    markers=['o','s'], # 标记点的样式
    kind='scatter', # 设定非对角线图表,可选的kde,hist,scatter
    diag_kind='hist', # 设定对角线上面的图标,一遍显示为 kde和hist
)
g.map_lower(sns.kdeplot)
g.fig.set_size_inches(10,10)
g.fig.set_dpi(200)
```


​    
![png](output_46_0.png)
​    



```python
g = sns.pairplot(
    data = data,
    kind='reg', # 设定非对角线图表,可选的kde,hist,scatter
    diag_kws=dict(color='orange'), # 对角线上图的颜色
    height=2, # 调整子图的高度
    aspect=1, # 宽度为height * aspect
    hue='性别',  # 按照性别的分类映射不同的颜色
    hue_order=['FEMALE','MALE'], # 分组的颜色顺序
    palette= ['#76c2df','#ef8b7c'], # 颜色可以指定列表['#76c2df','#ef8b7c'],'Set1'#
    markers=['o','s'], # 标记点的样式
    diag_kind='hist', # 设定对角线上面的图标,一遍显示为 kde和hist
    plot_kws=dict(
        scatter_kws = {'alpha':0.4,'s':12},
        line_kws={
            'linestyle':"-",
            'linewidth': 2,
        }
    )
)
g.fig.set_size_inches(10,10)
g.fig.set_dpi(200)
```


​    
![png](output_47_0.png)
​    


## 边际图


```python
sns.jointplot(
    data = data,
    x = '喙长 (毫米)',
    y = '喙深 (毫米)',
    hue = '性别',  # 分组的变量
    kind='scatter', # kde
    palette=['#76c2df','#ef8b7c'], # 设定分组配色
    marginal_kws=dict(color='#76c2df',alpha=.8), # 两侧图表可视化
    joint_kws=dict( # 中心图设置','#ef8b7c
        color='#ef8b7c', # 点的颜色
        s = 120,  # 点的大小
        alpha=.8,  # 点的透明度 
    )
)
```




    <seaborn.axisgrid.JointGrid at 0x25366270e00>




​    
![png](output_49_1.png)
​    



```python
sns.jointplot(
    data = data,
    x = '喙长 (毫米)',
    y = '喙深 (毫米)',
    hue = '性别',  # 分组的变量
    kind='kde', # kde
    palette=['#76c2df','#ef8b7c'], # 设定分组配色
    marginal_kws=dict(color='#76c2df',alpha=.8), # 两侧图表可视化
    joint_kws=dict( # 中心图设置','#ef8b7c
        color='#ef8b7c', # 点的颜色
        fill = True,
        alpha=.8,  # 点的透明度 
    )
)
```




    <seaborn.axisgrid.JointGrid at 0x25366e566c0>




​    
![png](output_50_1.png)
​    



```python
sns.jointplot(
    data = data,
    x = '喙长 (毫米)',
    y = '喙深 (毫米)',
    kind='reg', # kde
    palette=['#76c2df','#ef8b7c'], # 设定分组配色
    marginal_kws=dict(color='red',
                     ), # 两侧图表可视化
    joint_kws=dict( # 中心图设置','#ef8b7c
        color='#ef8b7c', # 点的颜色
        line_kws = dict(color='r',linewidth=1.5)
    )
)
```




    <seaborn.axisgrid.JointGrid at 0x2536aa66780>




​    
![png](output_51_1.png)
​    



```python
g = sns.JointGrid(data=data,x = '喙长 (毫米)',y = '喙深 (毫米)')
g.plot_joint(sns.scatterplot,
            color = 'red',
            marker = 'o',
            )  # ['#76c2df','#ef8b7c']

g.ax_marg_x.hist(data['喙长 (毫米)'],
                 color = '#76c2df',
                 bins=15,
                 edgecolor='black',
                )

g.ax_marg_y.hist(data['喙深 (毫米)'],orientation='horizontal',
                color = '#ef8b7c',
                 bins=15,
                 edgecolor='black',
                )
g.fig.set_dpi(150)
plt.show()
```


​    
![png](output_52_0.png)
​    



```python
g = sns.JointGrid(data=data,x = '喙长 (毫米)',y = '喙深 (毫米)')
g.plot_joint(sns.scatterplot,
            color = 'red',
            marker = 'o',
            )
sns.kdeplot(x =data['喙长 (毫米)'],
           ax=g.ax_marg_x
           )
sns.boxplot(y=data['喙深 (毫米)'],
           ax=g.ax_marg_y
           )
```




    <Axes: ylabel='喙深 (毫米)'>




​    
![png](output_53_1.png)
​    



```python
g = sns.JointGrid(data=data,x = '喙长 (毫米)',y = '喙深 (毫米)',hue='性别')

g.plot(
    sns.kdeplot, # 中心图表
    sns.kdeplot ,# 两边都
    fill=True,
    alpha=.5,
)
```




    <seaborn.axisgrid.JointGrid at 0x2534bc88290>




​    
![png](output_54_1.png)
​    



```python
import matplotx
plt.style.use(matplotx.styles.pitaya_smoothie['light'])
```


```python
plt.figure(figsize=(12,6))
g = sns.JointGrid(data=data,x = '喙长 (毫米)',y = '喙深 (毫米)',hue='性别',
                 palette=['#76c2df','#ef8b7c'],
                  height=5,
                 )
g.plot_joint(sns.kdeplot,fill=True,alpha=.5,)

sns.boxplot(data=data,
           y = '性别',
           x = '喙长 (毫米)',
           hue='性别',
           palette=['#76c2df','#ef8b7c'],
           ax = g.ax_marg_x,
           legend=False,
           )
sns.stripplot(
    data=data,
           y = '性别',
           x = '喙长 (毫米)',
           hue='性别',
           palette=['#76c2df','#ef8b7c'],
           ax = g.ax_marg_x,
           legend=False,
)
sns.boxplot(data=data,
           x = '性别',
           y = '喙深 (毫米)',
           hue='性别',
           palette=['#76c2df','#ef8b7c'],
           ax = g.ax_marg_y,
           legend=False,
           )
plt.show()
```


    <Figure size 1200x600 with 0 Axes>




![png](output_56_1.png)
    



```python

```
