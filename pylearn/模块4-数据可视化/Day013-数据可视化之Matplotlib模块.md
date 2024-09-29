---
title: "河南师范大学Python人工智能方向-数据可视化"
author: [梁霄]
date: "{2024年9月26日}"
subject: "Markdown"
keywords: [Markdown, Example]
subtitle: "Python数据可视化之Matplotlib篇"
page-background: "backgrounds/background1.pdf"
page-background-opacity : 0.6
toc: true
toc-own-page: true
titlepage: true
titlepage-rule-color: "360049"
titlepage-background: "backgrounds/background1.pdf"
titlepage-text-color: "7137C8"
titlepage-rule-color: "7137C8"
titlepage-rule-height: 2
titlepage-logo: "backgrounds/logo.jpg"
logo-width: 40mm
table-use-row-colors: false
listings-disable-line-numbers: true
colorlinks: true
---

[toc]

# Day013-数据可视化之Matplotlib模块

昨日内容:
- Scienceplot主题的使用
- 主题的使用方法:
    - 全局使用: plt.style.use
    - 局部使用: with plt.style.context
- 字体从处理:
    - 方案1: 全局字体的设定: plt.rcParams[font.sans-serif] = '字体'
    - 全局字体位置在什么地方找
    - 方案2: 全局字体+局部字体设定(重要)
    - 方案3: 调用LaTeX绘制图表(了解)
- 图表的存储:
    - 存储的格式: png/pdf/svg
    - 存储DPI设定(200-300)
    - 图表裁剪白边
    - 图表背景色设置透明
- 画布的创建: plt.figure
    - 画布的大小
    - 画布的分辨率
- 子图的创建: 
    - plt.subplots(重要)
    - plt.subplot(重要)
    - plt.axes(了解)
- 基本折线图的绘制:
    - 折线图绘制方法:
    - 折线图参数设定
    - plt.fill_bewtten:填充
    - plt.legend图例参数的设定

## 折线图进阶
### 进阶折线图-双Y轴折线图


```python
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sys
print('Python version:', sys.version)
print('Pandas version:', pd.__version__)
print('Numpy version:', np.__version__)
print('Matplotlib version:', matplotlib.__version__)
```


```python
data = pd.read_csv('./data/economics.csv')
```

任务目标: 完成随时间变化: 个人存储率psavert和失业人数unemploy的变化折线图

|    | date       |   pce |    pop |   psavert |   uempmed |   unemploy |
|---:|:-----------|------:|-------:|----------:|----------:|-----------:|
|  0 | 1967-07-01 | 507.4 | 198712 |      12.5 |       4.5 |       2944 |
|  1 | 1967-08-01 | 510.5 | 198911 |      12.5 |       4.7 |       2945 |
|  2 | 1967-09-01 | 516.3 | 199113 |      11.7 |       4.6 |       2958 |
|  3 | 1967-10-01 | 512.9 | 199311 |      12.5 |       4.9 |       3143 |
|  4 | 1967-11-01 | 518.1 | 199498 |      12.5 |       4.7 |       3066 |


```python
import matplotx
plt.rcParams['font.sans-serif'] = 'Times New Roman'
plt.rcParams['font.size'] = 15
plt.style.use(matplotx.styles.pitaya_smoothie['light'])
fig = plt.figure(figsize=(16,9),dpi=100) # 创建一个画布,

plt.plot(data['date'],data['psavert'],label='个人存储率',
        color='red',linewidth = 1.2,linestyle=(0, (3, 1, 1, 1, 1, 1))
        )
plt.xticks(np.arange(0,data.shape[0],40),rotation=45) # x轴刻度标签每隔40个显示一次,并做倾斜45,以显示更多
plt.ylim(0,18)
plt.ylabel('个人存储率',fontdict={'family':'STsong'},color='red')
plt.tick_params(axis='y',labelcolor='red')
plt.xlabel('日期',fontdict={'family':'STsong'})
plt.title('个人存储率与失业人数对比折线图',fontdict={'family':'STsong','size':20})

plt.twinx() # 让两个图表共享x轴,

plt.plot(data['date'],data['unemploy'],label='失业人数',
        color='blue',linewidth = 1.2,linestyle=(0, (5, 1))
        )
plt.xticks(np.arange(0,data.shape[0],40),rotation=45) # x轴刻度标签每隔40个显示一次,并做倾斜45,以显示更多
plt.ylim(0,18000)
plt.ylabel('失业人数',fontdict={'family':'STsong'},color='blue')
plt.tick_params(axis='y',labelcolor='blue')
fig.legend(loc=1,prop={'family':'STsong'},bbox_to_anchor=(0.26,0.87),
          shadow=True,fancybox=True,labelcolor='linecolor',frameon=True
          )
plt.show()
```

- 共享x轴,plt.twinx 可以开启共享x轴,在这个前后分别是两个图表,图一用左边的Y轴,图二用右边的y轴
- 图例的设定,对于一个画布上两个单独的图像,图例设定可以使用画布中的图例对象进行添加,
- 坐标轴刻度标签的设定,plt.tick_params的使用

- 图表中折线颜色一致
- x轴,y轴,标题,图例,这些都没有
- 字体没处理
- 网格线没有对齐
- 坐标轴很混乱,不知道那个坐标轴对应的是那个折线

### 进阶折线图-双子图


```python
plt.rcParams['font.sans-serif'] = 'Times New Roman'
plt.rcParams['font.size'] = 15
```


```python
plt.figure(figsize=(20, 9), dpi=100)

plt.subplot(211)
plt.plot(data['date'], data['psavert'], label='个人存储率',
         color='red', linewidth=1.2, linestyle=(0, (3, 1, 1, 1, 1, 1)))
# 设置 x 轴刻度标签每隔 40 个显示一次，并倾斜 45 度
plt.tick_params(axis='x',direction='out',pad=14)
plt.xticks(np.arange(0, data.shape[0], 50))

plt.ylim(0, 18)  # 设置 y 轴范围为 0 到 18
plt.ylabel('个人存储率',fontdict={'family':'STsong'}, color='red')  # 设置 y 轴标签和颜色
plt.tick_params(axis='y', labelcolor='red',direction='in')  # 设置 y 轴刻度标签颜色
plt.grid()

plt.title('个人存储率与失业人数对比折线图', fontdict={'family':'STsong','size': 20})  # 设置标题

plt.subplot(212)
# 绘制失业人数折线图
plt.plot(data['date'], data['unemploy'], label='失业人数',
         color='blue', linewidth=1.2, linestyle=(0, (5, 1)))

plt.xticks(np.arange(0,data.shape[0],50)) # x轴刻度标签每隔40个显示一次,并做倾斜45,以显示更多
plt.ylim(0,18000)
plt.ylabel('失业人数',fontdict={'family':'STsong'},color='blue')
plt.tick_params(axis='y',labelcolor='blue',direction='in')
plt.tick_params(axis='x',
                bottom=False, # 关闭底部的刻度指示器
                labelbottom=False, # 关闭底部的刻度标签
                direction='out', # 刻度指示器的朝向
                top=True) # 开启顶部的刻度指示器.
plt.grid()
plt.show()
```

### 折线图进阶-堆叠面积图


```python
data = pd.read_csv('./data/store.csv')
```

|    | Day   |   Email |   Union Ads |   Video Ads |   Direct |   Search Engine |
|---:|:------|--------:|------------:|------------:|---------:|----------------:|
|  0 | 周一  |     120 |         220 |         150 |      320 |             820 |
|  1 | 周二  |     132 |         182 |         232 |      332 |             932 |
|  2 | 周三  |     101 |         191 |         201 |      301 |             901 |
|  3 | 周四  |     134 |         234 |         154 |      334 |             934 |
|  4 | 周五  |      90 |         290 |         190 |      390 |            1290 |
|  5 | 周六  |     230 |         330 |         330 |      330 |            1330 |
|  6 | 周日  |     210 |         310 |         410 |      320 |            1320 |

1. 第一条折线很轻松可以绘制出来
2. 第二条折线: 是第二条折线本身+第一条折线的数据.
3. 第三条折线图: 前三条折线图数据之后
4. ...

第N条折线图,数据应该为前N条数据之和


```python
data.iloc[:,1:] = data.iloc[:,1:].cumsum(axis=1)
```


```python
lists = data.columns.tolist()
lists[0] = 0
lists = list(zip(lists[:-1],lists[1:]))
```


```python
colors = ['#91a1df','#c6e8ad','#fbe79d','#f3a19e','#b2dff4']
```


```python
plt.rcParams['font.sans-serif'] = 'Times New Roman'
plt.figure(figsize=(12, 5), dpi=100)

for index, item in enumerate(data.columns[1:]):
    
    plt.plot(data['Day'], data[item],lw=2,color=colors[index],zorder=1)
    plt.scatter(data['Day'],data[item],zorder=2,s=10,)
    if index == 0:
        plt.fill_between(x=data['Day'],
                    y1 = 0,y2 = data[lists[index][1]],color=colors[index],zorder=0)
    else:
        plt.fill_between(x=data['Day'],
                        y1 = data[lists[index][0]],
                        y2 = data[lists[index][1]],color=colors[index],zorder=0,
                        )

plt.xticks(fontproperties='STsong')
plt.show()
```

### 堆叠面积图改


```python
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sys
print('Python version:', sys.version)
print('Pandas version:', pd.__version__)
print('Numpy version:', np.__version__)
print('Matplotlib version:', matplotlib.__version__)
```

    Python version: 3.12.3 | packaged by conda-forge | (main, Apr 15 2024, 18:20:11) [MSC v.1938 64 bit (AMD64)]
    Pandas version: 2.2.2
    Numpy version: 1.26.4
    Matplotlib version: 3.8.4



```python
data = pd.read_csv('./data/store.csv')
data.iloc[:,1:] = data.iloc[:,1:].cumsum(axis=1)
data.insert(1,0,0)
```


```python
lists = data.columns.tolist()[1:]
lists = list(zip(lists[:-1],lists[1:]))
colors = ['#91a1df','#c6e8ad','#fbe79d','#f3a19e','#b2dff4']
```


```python
plt.rcParams['font.sans-serif'] = 'Times New Roman'
plt.figure(figsize=(20,9), dpi=100)
for index, item in enumerate(data.columns[2:]):
    plt.plot(data['Day'], data[item],lw=2,color=colors[::-1][index],zorder=2)
    plt.scatter(data['Day'],data[item],zorder=3,s=10,)
    plt.fill_between(x=data['Day'],
                    y1 = data[lists[index][0]],
                    y2 = data[lists[index][1]],color=colors[index],zorder=1,
                     label=item,
                    )
plt.xticks(fontproperties='STsong')
plt.legend()
plt.xlim(0,6)
plt.ylim(0,3000)
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('The Stacked Area Chart',fontsize=22)
plt.grid(axis='y',color='gray',alpha=.4,)
plt.show()
```


```python
data = pd.read_csv('./data/store.csv')
data.iloc[:,1:] = data.iloc[:,1:].cumsum(axis=1)
data.insert(1,0,0)
```


```python
lists = data.columns.tolist()[1:]
lists = list(zip(lists[:-1],lists[1:]))
```


```python
plt.figure(figsize=(20,9), dpi=100)

# plt.plot(data['Day'], data['Email'],lw=2,color='red',)
# plt.plot(data['Day'], data['Union Ads'],lw=2,color='green')
# plt.plot(data['Day'], data['Video Ads'],lw=2,color='blue',)
# plt.plot(data['Day'], data['Direct'],lw=2,color='cyan',)
# plt.plot(data['Day'], data['Search Engine'],lw=2,color='orange',)

for index,item in enumerate(data.columns[2:]):
    plt.plot(data['Day'], data[item],lw=2,color='red',)
    plt.fill_between(data['Day'],y1=data[lists[index][0]],
                     y2= data[lists[index][1]])
# plt.fill_between(data['Day'],y1=0,y2=data['Email'])
# plt.fill_between(data['Day'],y1=data['Email'],y2=data['Union Ads'])
# plt.fill_between(data['Day'],y1=data['Union Ads'],y2=data['Video Ads'])
# plt.fill_between(data['Day'],y1=data['Video Ads'],y2=data['Direct'])
# plt.fill_between(data['Day'],y1=data['Direct'],y2=data['Search Engine'])
plt.xticks(fontproperties='STsong')
plt.xlim(0,6)
plt.ylim(0,3000)
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('The Stacked Area Chart',fontsize=22)
plt.grid(axis='y',color='gray',alpha=.4,)
plt.xticks(fontproperties='STsong')
plt.show()
```

## 柱形图
主要用于多个数据系列对比使用

### 基础柱形图-单数据系列


```python
data = pd.read_csv('./data/stack_data_bar.csv')
```

|    | Country       |   Pensions |   Income |   Health  |   Other services |
|---:|:--------------|-----------:|---------:|----------:|-----------------:|
|  0 | Italy         |         14 |        5 |         9 |                3 |
|  1 | Spain         |          8 |        6 |         7 |                8 |
|  2 | United States |         15 |        4 |         7 |                1 |
|  3 | France        |         11 |        5 |         8 |                3 |
|  4 | Germany       |          9 |        7 |         7 |                2 |
|  5 | Sweden        |          6 |        6 |         8 |                4 |
|  6 | China         |          7 |        3 |         8 |                1 |
|  7 | Britain       |          8 |        5 |         6 |                3 |


```python
colors = ['#464ca6','#6472ea','#7fc9da','#eec568','#df8342','#7fc6e1','#ee9589']
```


```python
import matplotx
plt.style.use(matplotx.styles.pitaya_smoothie['light'])
plt.rcParams['font.sans-serif'] = 'Times New Roman'
plt.rcParams['font.size'] = 14
plt.figure(figsize=(14,6), dpi=100)
plt.bar(x=data['Country'],           # x轴数据
        height = data['Pensions'],   # 柱子的高度
        width = .6,                  # 柱子的宽度
        color = '#7fc9da',           # 柱子的颜色
        edgecolor = 'black',         # 柱子的颜色
        linewidth = 1,               # 柱子的边框的粗细
        alpha = .9,                  # 柱子的透明度
        yerr = [0.3] * data.shape[0],# 添加误差线
        ecolor = 'red',              # 误差线的颜色
        label = 'Pensions',          # 数据标签
        align='center',              # 柱子的位置
#         bottom = [2,3,4,6,5,4,2,1]   # 数据的起始位置,一般用于绘制瀑布图
       )
plt.xlabel('Country')
plt.ylabel('Pensions')
plt.title('The Basic column chart -various parament settings',fontsize=20)
plt.legend()

for i in range(data.shape[0]):
    plt.text(data['Country'][i], # X坐标
            data['Pensions'][i]/2, # y坐标
            data['Pensions'][i], # y的实际值
            ha='center',
            va='bottom',
            )
plt.show()
```

- 每个柱子显示数字
- 柱子上加折线
- 柱子的颜色/柱子的变框/边框的粗细/颜色/柱子的宽度/柱子与柱子之间的间距/透明度

### 折线图进阶-圆角柱形图


```python
colors = ['#464ca6','#6472ea','#7fc9da','#eec568','#df8342']
from matplotlib.patches import FancyBboxPatch
```


```python
plt.rcParams['font.sans-serif'] = 'Times New Roman'
plt.rcParams['font.size'] = 14
plt.figure(figsize=(6,6), dpi=100)
rects = plt.bar(x=data['Country'][:5],           # x轴数据
        height = data['Pensions'][:5],   # 柱子的高度
        width = .4,                  # 柱子的宽度
        color = colors,           # 柱子的颜色
        label = 'Pensions',          # 数据标签
        align='center',              # 柱子的位置
        bottom=[1.5] * 5
       )

ax = plt.gca() # 获取当前的坐标轴对象
for rect in rects:
    rect.remove()
for index,rect in enumerate(rects):
    bb = rect.get_bbox()
    patch = FancyBboxPatch((bb.xmin,bb.ymin), # 左下角的坐标
                          abs(bb.width),abs(bb.height),
                          boxstyle="Round, pad=0, rounding_size=0.1", # 补丁的样式
                          ec=colors[index],fc=colors[index],linewidth=2,
                           mutation_aspect=4,
                           mutation_scale=2.2,
                          )
    ax.add_patch(patch)
ax = plt.gca()
ax.set_facecolor('#1a1c41')
plt.ylim(0,26)
plt.text(x=-.34,y=21,
         color='white',
         s='Uses Excel, Python, SQL, power BI to share the whole process data analysis and correct solutions')
plt.text(x = - 0.34,y=24,s='Doughnut Classification',color='white', fontweight='bold')
plt.tick_params(axis='y',labelleft=False,left=False)
plt.tick_params(axis='x',bottom=False,pad=-18,)
plt.xticks(color='white')
for i in range(5):
    plt.text(data['Country'][i], # X坐标
            data['Pensions'][i]+3, # y坐标
            data['Pensions'][i], # y的实际值
            ha='center',
            va='bottom',
            color='white'
            )
plt.savefig('./figure/fig-s-1.png',dpi=200,bbox_inches='tight',pad_inches=0.0)
plt.show()
```


​    
![png](output_36_0.png)
​    



```python
# 圆角柱形图设置函数
def get_round_rect(rects,ec='black',fc='#96c8d6'):
    bb = rects.get_bbox()
    patch = FancyBboxPatch((bb.xmin,bb.ymin), # 左下角的坐标
                          abs(bb.width),abs(bb.height),
                          boxstyle="Round, pad=0, rounding_size=0.05", # 补丁的样式
                          ec=ec,fc=fc,linewidth=1,
                           mutation_aspect=4,
                           mutation_scale=1,
                          )
    return patch
```

### 多系列柱形图


```python
x = np.arange(data.shape[0])
```


```python
with plt.style.context(matplotx.styles.pitaya_smoothie['light']):
    plt.figure(figsize=(14,7), dpi=100)

    rects1 = plt.bar(x-0.2,data['Pensions'],width=0.4,label='Pensions',fc='#a3c7d4',
                    ec='black',
                    )
    rects2 = plt.bar(x,data['Income'],align='edge',width=0.4,label='Income',fc='orange',
                    ec='black'
                    )


    ax = plt.gca()
    for rect in zip(rects1,rects2):  
        rect[0].remove()
        rect[1].remove()
        patch1 = get_round_rect(rect[0],fc='#a3c7d4')
        patch2 = get_round_rect(rect[1],fc='orange')
        ax.add_patch(patch1)
        ax.add_patch(patch2)
    
    plt.xlabel('Country')
    plt.ylabel('Vlaue')
    plt.title('柱形图进阶-分组柱形图',fontdict={'family':'STsong','size':20})
    plt.xticks(ticks=x,labels=data['Country'])
    plt.ylim(0,16)
    for i in range(data.shape[0]):
        plt.text(x[i]-.2,data['Pensions'][i],data['Pensions'][i],va='bottom',ha='center')
        plt.text(x[i]+.2,data['Income'][i],data['Income'][i],va='bottom',ha='center')
plt.legend()
plt.show()
```


​    
![png](output_40_0.png)
​    


## 柱形图进阶-堆叠柱形图


```python
data = pd.read_csv('./data/奖牌.csv')
```

|    | 赛事           |   参赛人数 |   金牌 |   银牌 |   铜牌 |   总计 |   排名 |
|---:|:---------------|-----------:|-------:|-------:|-------:|-------:|-------:|
|  0 | 1984年洛杉矶   |        216 |     15 |      8 |      9 |     32 |      4 |
|  1 | 1988年汉城     |        273 |      5 |     11 |     12 |     28 |     11 |
|  2 | 1992年巴塞罗那 |        244 |     16 |     22 |     16 |     54 |      4 |
|  3 | 1996年亚特兰大 |        294 |     16 |     22 |     12 |     50 |      4 |
|  4 | 2000年悉尼     |        271 |     28 |     16 |     14 |     58 |      3 |
|  5 | 2004年雅典     |        384 |     32 |     17 |     14 |     63 |      2 |
|  6 | 2008年北京     |        639 |     48 |     22 |     30 |    100 |      1 |
|  7 | 2012年伦敦     |        396 |     38 |     31 |     22 |     91 |      2 |
|  8 | 2016年里约     |        412 |     26 |     18 |     26 |     70 |      3 |
|  9 | 2020年东京     |        431 |     38 |     32 |     18 |     88 |      2 |

- 要求绘制最近的4次奥运会,金牌数量,银牌数量,铜牌数量分组柱形图/堆积柱形图


```python
data1 = data.iloc[-4:,]
x = np.arange(data1.shape[0])
```


```python
plt.figure(figsize=(20,7), dpi=100)

plt.bar(x,data1['金牌'],width=0.2)

plt.bar(x+0.1,data1['银牌'],align='edge',width=0.2)
plt.bar(x-0.2,data1['铜牌'],width=0.2)
plt.show()
```


​    
![png](output_46_0.png)
​    



```python
# 堆积柱形图

plt.figure(figsize=(20,7), dpi=100)

plt.bar(data['赛事'],data['铜牌'],)
plt.bar(data['赛事'],data['银牌'],bottom=data['铜牌'])
plt.bar(data['赛事'],data['金牌'],bottom=data['铜牌']+data['银牌'])

plt.xticks(fontproperties='STsong',rotation=45)
for i in range(data.shape[0]):
    plt.text(data['赛事'][i],data['铜牌'][i]/2,data['铜牌'][i])
    plt.text(data['赛事'][i],data['铜牌'][i] + data['银牌'][i]/2,data['铜牌'][i])
    plt.text(data['赛事'][i],data['总计'][i] - data['金牌'][i]/2,data['金牌'][i])
    plt.text(data['赛事'][i],data['总计'][i],f"总数: {data['总计'][i]}",fontproperties='STsong',
            ha='center',va='bottom'
            )
plt.show()
```


​    
![png](output_47_0.png)
​    

