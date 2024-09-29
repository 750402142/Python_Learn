---
title: "河南师范大学Python人工智能方向-数据可视化"
author: [梁霄]
date: "{2024年9月25日}"
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

# Day012-数据可视化之Matplotlib模块

1. Pandas结合数据库进行数据的读和写操作 [必须要掌握的]
2. Matplotlib数据数据可视化概述
    - Matplotlib是什么?
    - 如何绘制一张图表
    - 绘图的步骤 [重点]
    - 图表主题[建议掌握]
        - 内置主题
        - matplotx里面的主题
        - scienceplot里面的主题(未演示)
        - 局部使用主题: with plt.style.context
        - 全局使用主题: plt.style.use
    - 全局的配置项
        - plt.rcParams[font.sans-serif]: 全局字体设定
        - plt.rcParams[axes.unicode_minute]: 负数符号的显示
        

1. 创建画布
2. 绘制基本图表: [重要]
3. 图表的展示
4. 添加图表元素和修饰图表 [重要]
5. 图表的存储(必须要放在图表展示的前面)

1. 主题的使用SciencePlot模块
2. 字体的解决方案
3. 创建画布/创建子图
4. 图表的保存: 存储图片存在白边的问题!图片的背景色
5. 基本图表的绘制

## 图表主题的使用-SciencePlots

模块的安装: pip install SciencePlots


```python
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sys
import scienceplots
print(scienceplots.stylesheets.keys())
print('Python version:', sys.version)
print('Pandas version:', pd.__version__)
print('Numpy version:', np.__version__)
print('Matplotlib version:', matplotlib.__version__)
```


```python
x = np.arange(0,2,0.01)
y = np.sin(2 * np.pi * x) + (2 * np.pi * x)
y1 = np.sin(2 * np.pi * x) - (2 * np.pi * x)
y2 = np.cos(2 * np.pi * x) + (2 * np.pi * x)
y3 = np.cos(2 * np.pi * x) - (2 * np.pi * x)
```


```python
plt.rcParams['font.size'] = 16
with plt.style.context(['nature', 'grid','no-latex']):
    plt.figure(figsize=(10,7),dpi=400) # 1. 创建画布
    plt.plot(x,y) # 2. 绘制图形1
    plt.plot(x,y1) # 2. 绘制图形2
    plt.plot(x,y2) # 2. 绘制图形3
    plt.plot(x,y3) # 2. 绘制图形4
    plt.xlabel('This is x label Voltage (mV)')
    plt.title(r'Current ($\mu$A)')
    plt.ylabel('这是Y轴的标签',fontdict={'family':'SimHei','size':14})
    plt.show() # 3. 展示图形
```


```python
# 定义极坐标的角度范围
theta = np.linspace(0, 2 * np.pi, 2000)
# 心形线的极坐标方程
r = 1 - np.sin(theta)
x = r * np.cos(theta)
y = r * np.sin(theta)
```

## 字体的处理

1. 解决方案1: 全局设定中文字体,以避免中文不显示问题,支持字体可以在C盘用户目录下.matplotlib文件夹中找font-list文件.
2. 解决方案2: 由于全局设定会导致图中所有的元素都是指定的字体,因此可以通过全局设定+局部设定
    -  如果中文元素多： 全局中文+局部英文 STsong+Times New Roman
    -  如果图中英文+数字元素多: 全局英文+局部中文: Times New Roman + STsong
3. 解决方案3: 中文元素为宋体英文元素为新罗马体,调用LaTeX进行绘制,优点渲染非常完美,缺点安装成本太大,渲染速度慢
    - 1. 安装MiKTeX
    - 2. 调用LaTeX进行图表的绘制


```python
import matplotlib
print(matplotlib.get_configdir()) # 字体的目录所在的位置,
```


```python
title = r"""这是标题字体,This Is Title font,$\iint_D\left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right) d x d y=\oint_L P d x+Q d y$"""
```

### 解决方案1: 全局字体设定


```python
# 方案1: 全局设定
import matplotx
plt.rcParams['font.sans-serif'] = 'STSong' # 设置全局的字体为黑体
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 14
with plt.style.context(matplotx.styles.pitaya_smoothie['light']):
    plt.figure(figsize=(9,7),dpi=100) # 1. 创建画布
    plt.plot(x,y) # 2. 绘制图形1
    plt.xlabel('This is x label Voltage (mV)')
    plt.title(label=title)
    plt.ylabel('这是Y轴的标签',)
    plt.xlim(-2,2)
    plt.ylim(-3,1)
    plt.axis('equal')  # 保持x和y轴的比例相同
    plt.show() # 3. 展示图形
```


```python
fontdict={'family':'SimHei','size':14}
```

### 解决方案2: 全局字体+局部字体


```python
# 方案2: 全局英文+局部中文
import matplotx
plt.rcParams['font.sans-serif'] = 'Times New Roman' # 设置全局的字体为黑体
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 14
with plt.style.context(matplotx.styles.pitaya_smoothie['light']):
    plt.figure(figsize=(9,7),dpi=100) # 1. 创建画布
    plt.plot(x,y) # 2. 绘制图形1
    plt.xlabel('This is x label Voltage (mV)')
    plt.title(label=title,fontproperties='STsong') # 字体设置方式1
    plt.ylabel('这是Y轴的标签',fontdict={'family':'STsong'}) # 字体设置方式2
    plt.xlim(-2,2)
    plt.ylim(-3,1)
    plt.axis('equal')  # 保持x和y轴的比例相同
    plt.show() # 3. 展示图形
```

### 解决方案3: LaTeX绘制


```python
import pandas as pd
import numpy as np
import matplotlib
from matplotlib import rcParams
import matplotlib.pyplot as plt
import sys
import matplotx
print('Python version:', sys.version)
print('Pandas version:', pd.__version__)
print('Numpy version:', np.__version__)
print('Matplotlib version:', matplotlib.__version__)

# 定义极坐标的角度范围
theta = np.linspace(0, 2 * np.pi, 2000)
# 心形线的极坐标方程
r = 1 - np.sin(theta)
x = r * np.cos(theta)
y = r * np.sin(theta)
title = r"""这是标题字体,This Is Title font,$\iint_D\left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right) d x d y=\oint_L P d x+Q d y$"""
```

    Python version: 3.12.3 | packaged by conda-forge | (main, Apr 15 2024, 18:20:11) [MSC v.1938 64 bit (AMD64)]
    Pandas version: 2.2.2
    Numpy version: 1.26.4
    Matplotlib version: 3.8.4



```python
matplotlib.use('pgf')
pgf_config = {
    'font.family':'serif', # 设置字体家族
    'font.size':14, # 字体大小
    'pgf.rcfonts':False, # 禁用默认字体
    'text.usetex':True, # 使用LaTeX渲染文本
    'pgf.preamble': # 添加相关的宏包进行字体配置
    '\n'.join([
        r"\usepackage{unicode-math}", # 加载数学宏包
        r"\setmathfont{Times New Roman}", # 谁定数学字体为Times New Roman 
        r"\setmainfont{Times New Roman}", # 设置全文的主要字体为Times New Roman 
        r"\usepackage{ctex}", # 加载CTeX宏包,处理中文字体
        r"\setCJKmainfont{SimSun}", # 设置中文字体为宋体
    ]),
}
rcParams.update(pgf_config)
```


```python
# 定义 theta 的范围
theta = np.linspace(0, 2 * np.pi, 10000)
# 计算 r 的值
r = np.exp(np.sin(theta)) - 2 * np.cos(4 * theta) + np.sin((2 * theta - np.pi) / 24) ** 5
# 将极坐标转换为直角坐标
x = r * np.cos(theta)
y = r * np.sin(theta)
```

- 阶段练习任务:
  
    要求绘制: y = x ** 3 - x ** 2 + 1 在 -10 到 10之间的图像
    
    图表要求谁定x轴名称,y轴名称,图表的标题为姓名+学号,图表要有图例和网格线


```python
x = np.arange(-10,10,0.1)
y = x ** 3 - x ** 2 + 1
```


```python
plt.figure(figsize=(12,6),dpi=100)

plt.plot(x,y,label=r'$y=x^3 - x^2 + 1$')
plt.xlabel('x')
plt.ylabel('y')
plt.title(r'The line of $y=x^3 - x^2 + 1$')
plt.grid()
plt.legend()
plt.savefig('./figure/fig-2.png',dpi=200)
```


```python
# 设置点的个数
m = 20
n = 256 * m + 1  # 总点数
# 变量的取值范围
tx = np.linspace(0, 24 * np.pi, n)
# 初始化 x 和 y 数组
x = np.zeros(n)
y = np.zeros(n)
# 计算函数的值
for i in range(n):
    t = tx[i]
    x[i] = np.sin(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t) - (np.sin(t / 12))**5)
    y[i] = np.cos(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t) - (np.sin(t / 12))**5)
```


```python
plt.figure(figsize=(12,10),dpi=100)
plt.plot(x,y,)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend()
# plt.savefig('./figure/fig-3.png',dpi=2000)
# plt.savefig('./figure/fig-4s.png',dpi=200,) # 不加任何东西
# plt.savefig('./figure/fig-4.png',dpi=200,bbox_inches='tight',pad_inches=0.0) # 设置边缘裁剪

# plt.savefig('./figure/fig-4s-face-edge.png',dpi=200,
#            facecolor='#b9d5e4', # 设定背景色,不是很常用
#            edgecolor='red',
#            )
# plt.savefig('./figure/fig-4s-por.png',dpi=200,orientation='portrait') # 不加任何东西
# plt.savefig('./figure/fig-4s-lad.png',dpi=200,orientation='landscape') # 不加任何东西

plt.savefig('./figure/fig-4-trans.png',dpi=200,bbox_inches='tight',pad_inches=0.0, # 设置透明背景
           transparent=True,  # 设置透明背景色
           ) #  重要,
```

    No artists with labels found to put in legend.  Note that artists whose label start with an underscore are ignored when legend() is called with no argument.


## 图表的存储

- 使用plt.savefig进行图表的存储

        savefig(*args, **kwargs) -> 'None'
    
1. 存储的路径: 存储的格式: png/pdf
    - pdf格式:矢量图图片不会失真占用的空间更小,建议使用
    - png格式: 占用的空间随着分辨率的增加,会变得更大,相对于jpg格式来说,更有优势
2. dpi: 分辨率: 分辨率越大图像的大小越大,也越清晰,一般是200-300左右,根据地画布大小进行调整
3. bbox_inches,用于控制图像的边缘裁剪,'tight': 保存紧凑的边缘,None保存整个图像
4. pad_inches: 边界框填充的大小
5. transparent: 是否设置图像背景透明
6. facecolor: 设定背景色
7. edgecolor: 边框颜色


```python
plt.figure(figsize=(12,10),dpi=100)
plt.plot(x,y,)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.savefig('./figure/fig-4-trans.png',dpi=200,
           bbox_inches='tight',
           pad_inches=0.0, # 设置透明背景
           transparent=True,  # 设置透明背景色
           ) #  重要,
```

- 必须安装一个LaTeX发行版:
    - TeX Live / MiKTeX
    - 必须更新宏包.使用MiKTeX console工具-更新一下所有的包
    - 关闭Jupyter Notebook然后重新打开
    - 执行PGF设定,然后完成绘图

## 画布的创建和子图的创建


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
# 设置点的个数
m = 20
n = 256 * m + 1  # 总点数
# 变量的取值范围
tx = np.linspace(0, 24 * np.pi, n)
# 初始化 x 和 y 数组
x = np.zeros(n)
y = np.zeros(n)
# 计算函数的值
for i in range(n):
    t = tx[i]
    x[i] = np.sin(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t) - (np.sin(t / 12))**5)
    y[i] = np.cos(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t) - (np.sin(t / 12))**5)
```

figure(num: 'int | str | Figure | SubFigure | None' = None, figsize: 'tuple[float, float] | None' = None, dpi: 'float | None' = None, *, facecolor: 'ColorType | None' = None, edgecolor: 'ColorType | None' = None, frameon: 'bool' = True, FigureClass: 'type[Figure]' = <class 'matplotlib.figure.Figure'>, clear: 'bool' = False, **kwargs) -> 'Figure'

- figsize: 画布的大小
- dpi: 画布的分辨率


```python
plt.figure(figsize=(8,6), # 画布的大小
          dpi = 100, # 画布的分辨率
          facecolor='#b1cfdf',  # 设定画布的背景色
          edgecolor='red',  # 边框的颜色
           linewidth=3, # 边框的粗细
          )
plt.plot(x,y, color='orange')

plt.xlabel('This is x label')
plt.ylabel('This is y label')
plt.title('The subplot of figure')

plt.show()
```


​    
![png](output_32_0.png)
​    



```python
plt.figure(num=1)
fig1 = plt.plot(x,y, color='orange',label='Line 1')

plt.title('The plot Figure1')
plt.legend()

fig2 = plt.plot(x,y+1, color='#b9d5e4',alpha=.3, label='Line 2')
plt.title('The plot Figure1')
plt.legend()

plt.figure(num=2) 
plt.scatter(x,y,c='cyan',label='scatter',s=1)
plt.legend()
plt.show()
```


​    
![png](output_33_0.png)
​    




![png](output_33_1.png)
    



```python
fig = plt.figure()
fig_number = fig.number
print(f"当前的画布编号{fig_number}")
plt.gcf() # 获取当前的画布对象
plt.plot(x,y)
```

    当前的画布编号1





    [<matplotlib.lines.Line2D at 0x24560cdbe30>]




​    
![png](output_34_2.png)
​    


### 画布的第二种创建方法


```python
# 设置点的个数
m = 20
n = 256 * m + 1  # 总点数
# 变量的取值范围
tx = np.linspace(0, 24 * np.pi, n)
# 初始化 x 和 y 数组
x = np.zeros(n)
y = np.zeros(n)
y1 = np.zeros(n)
y2 = np.zeros(n)
y3 = np.zeros(n)
# 计算函数的值
value_y = []
for i in range(n):
    t = tx[i]
    x[i] = np.sin(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t) - (np.sin(t / 12))**5)
    y[i] = np.cos(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t) - (np.sin(t / 12))**5)
    y1[i] = np.cos(t) * (np.exp(np.cos(t)) + 2 * np.cos(4 * t) - (np.sin(t / 12))**2)
    y2[i] = np.cos(t) * (np.exp(np.sin(t)) - 2 * np.cos(4 * t) + (np.sin(t / 12))**5)
    y3[i] = np.cos(t) * (np.exp(np.cos(t)) + 2 * np.cos(4 * t) + (np.sin(t / 12))**5)
value_y.extend([y,y1,y2,y3])
colors = ['#b5d1e2','orange','pink','#3992ea']
```


```python
plt.rcParams['font.sans-serif'] = 'Times New Roman'
fig,axs = plt.subplots(
    nrows=2, # 子图的行数为2
    ncols=2, #子图的列数为2
    figsize=(12,8), # 画布的大小
    dpi=100, # 画布的分辨率
    sharex=True, # 共享X轴
    sharey=True, # 共享Y轴
    facecolor='None', # 设置画布背景色为透明
    frameon=True, # 开启画布的边框
    linewidth = 4, # 设置边框的线条宽度
    edgecolor = 'cyan', # 设置边框的颜色
    width_ratios=[2,2], #  指定子图每列的宽度比为2:2
    height_ratios=[2,2], # 指定子图每行的高度比例为2:2
    subplot_kw={'facecolor':'none'}, # 设置子图的背景色为透明
    gridspec_kw={'wspace':0,'hspace':0}, # s设置子图的间距
)
 
for index,ax in enumerate(axs.flatten()):
    ax.plot(x,value_y[index],color=colors[index],linewidth=.8,)
    
plt.show()
```


​    
![png](output_37_0.png)
​    


### 子图创建方法2

plt.subplot(nrows,ncols,index)

- 子图网格的行数
- 子图网格的列数
- index:当前的子图在网格中的位置


```python
plt.subplot(221)
plt.plot(x, y, color='red')

plt.subplot(222)
plt.plot(x, y1, color='orange')

plt.subplot(223)
plt.plot(x, y2, color='pink')

plt.subplot(224)
plt.plot(x, y3, color='blue')

```




    [<matplotlib.lines.Line2D at 0x24566091010>]




​    
![png](output_39_1.png)
​    



```python
plt.figure(figsize=(12,7),dpi=100)
plt.subplot(121)
plt.plot(x, y, color='red')
plt.xlabel('fig1 x label')

plt.subplot(222)
plt.plot(x, y1, color='blue')
plt.xlabel('fig2 x label')

plt.subplot(224)
plt.plot(x, y3, color='pink')
```




    [<matplotlib.lines.Line2D at 0x245610c6ff0>]




​    
![png](output_40_1.png)
​    



```python
plt.subplot(122)
plt.plot(x, y, color='red')

plt.subplot(221)
plt.plot(x, y1, color='blue')

plt.subplot(223)
plt.plot(x, y3, color='pink')
```




    [<matplotlib.lines.Line2D at 0x245637f7350>]




​    
![png](output_41_1.png)
​    



```python
plt.subplot(311)
plt.plot(x, y, color='red')

plt.subplot(334)
plt.plot(x, y1, color='blue')

plt.subplot(335)
plt.plot(x, y1, color='blue')
plt.subplot(336)
plt.plot(x, y1, color='blue')

plt.subplot(313)
plt.plot(x, y3, color='pink')
```




    [<matplotlib.lines.Line2D at 0x24565d06b40>]




​    
![png](output_42_1.png)
​    


### 子图的绘制方式3


```python
plt.figure(figsize=(12,4),dpi=100,edgecolor='red',linewidth=2)

plt.axes([0,0,0.9,0.9]) # 这是第一个图表的位置,传入四个参数,分别是开始点的百分比坐标,对角线终端的百分比坐标
plt.plot([1,2,3,4],[1,4,9,16])
plt.annotate('', xy=(1, 1), xytext=(1.5, 9.1),
        arrowprops = dict(arrowstyle="->",linewidth=2,color='red',
        connectionstyle="arc"))
plt.annotate('', xy=(2, 4), xytext=(1.5, 9.1),
        arrowprops = dict(arrowstyle="->",linewidth=1,color='red',
        connectionstyle="arc"))
plt.axes([0.1,.48,.3,.3])
plt.plot([1,2,],[1,4])

plt.show()
```


​    
![png](output_44_0.png)
​    


- 主题的使用
- 字体的处理
- 图表的保存
- 画布的创建
- 子图的创建

## 折线图
主要用于显示数据在一个连续的时间段内容变化情况


```python
import pandas as pd
import matplotx
plt.style.use(matplotx.styles.pitaya_smoothie['light'])
data = pd.read_csv('./data/Line_Data.csv')
data.shape
```




    (122, 3)



### 基本折线图

|    | date       |   Amazon |   Apple |
|---:|:-----------|---------:|--------:|
|  0 | 2013-01-31 |       69 |   25.94 |
|  1 | 2013-02-28 |       67 |   28.66 |
|  2 | 2013-03-31 |       55 |   33.95 |
|  3 | 2013-04-30 |       48 |   31.01 |
|  4 | 2013-05-31 |       36 |   21    |


```python
plt.rcParams['font.sans-serif'] = 'Times New Roman'
plt.rcParams['font.size'] = 14
plt.rcParams['legend.title_fontsize'] = 14
plt.figure(figsize=(14,6),dpi=100)
plt.plot(data['date'],data['Amazon'],label='Amazon')
plt.plot(data['date'],data['Apple'],label='Apple')
plt.xticks(np.arange(0,data.shape[0],10),rotation=30,)
plt.legend(loc='upper left',ncols=2,labelcolor='linecolor',
          frameon=True, # 是否开启边框
          edgecolor='red', # 边框边缘的颜色
           shadow=True, # 是否开启阴影
           title='图例', # 设定图例的名称
           title_fontproperties='STsong', # 设定图例的字体
           fontsize=14, # 设定图例的字体大小
#            title_fontsize=16, # 图例的字体大小和字体只能同时设置一个           
#            facecolor='none', # 设定背景色
          )
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('The Basic Line Chart',fontsize=16)
plt.ylim(0,250)
plt.savefig('./figure/line_01.png',dpi=200,bbox_inches='tight',pad_inches=0)
plt.show()
```


​    
![png](output_50_0.png)
​    


- 当x轴刻度标签比较密集时如何处理:
    - 每隔一段显示一个刻度标签
    - 通过设定刻度标签的旋转度数来确定
- 关于图例的详细设定

### 面积图
在折线图的基础上添加区域填充


```python
plt.rcParams['font.sans-serif'] = 'Times New Roman'
plt.rcParams['font.size'] = 14
plt.rcParams['legend.title_fontsize'] = 14
plt.figure(figsize=(14,6),dpi=100)
plt.fill_between(data['date'],y1=data['Amazon'],y2=0,
                label='Amazon_area', # 标签名
                alpha=0.75, # 填充的透明读
                color='#00befe',
                linewidth=1, # 填充后边框线条的粗细
                 edgecolor='black'
                )
plt.fill_between(data['date'],y1=data['Apple'],y2=0,
                label='Apple_area', # 标签名
                alpha=0.75, # 填充的透明读
                linewidth=1, # 填充后边框线条的粗细
                 edgecolor='black'
                )
plt.xticks(np.arange(0,data.shape[0],10),rotation=30,)
plt.legend(loc='upper left',ncols=1,labelcolor='linecolor',
          frameon=True, # 是否开启边框
          edgecolor='red', # 边框边缘的颜色
           shadow=True, # 是否开启阴影
           title='图例', # 设定图例的名称
           title_fontproperties='STsong', # 设定图例的字体
           fontsize=14, # 设定图例的字体大小      
          )
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('The Basic Line_Area Chart',fontsize=16)
plt.ylim(0,250)
plt.xlim(0,122)
plt.savefig('./figure/line_area_01.png',dpi=200,bbox_inches='tight',pad_inches=0)
plt.show()
```


​    
![png](output_53_0.png)
​    


### 夹层填充色

- 只填充两条线条之间的区域
- Amazon大于Apple的区域填充颜色A,Amazon小于Apple的区域填充颜色B


```python
plt.rcParams['font.sans-serif'] = 'Times New Roman'
plt.rcParams['font.size'] = 14
plt.rcParams['legend.title_fontsize'] = 14
plt.figure(figsize=(14,6),dpi=100)
plt.fill_between(data['date'],y1=data['Amazon'],y2=data['Apple'],
                label='Amazon with Apple',
                alpha=0.75, # 填充的透明读
                color='#00befe',
                linewidth=1, # 填充后边框线条的粗细
                 edgecolor='black'
                )
plt.plot(data['date'],data['Amazon'],label='Amazon',color='red')
plt.plot(data['date'],data['Apple'],label='Apple',color='blue')

plt.xticks(np.arange(0,data.shape[0],10),rotation=30,)
plt.legend(loc='upper left',ncols=1,labelcolor='linecolor',
          frameon=True, # 是否开启边框
          edgecolor='red', # 边框边缘的颜色
           shadow=True, # 是否开启阴影
           title='图例', # 设定图例的名称
           title_fontproperties='STsong', # 设定图例的字体
           fontsize=14, # 设定图例的字体大小      
          )
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('The Basic Line_Area Chart',fontsize=16)
plt.ylim(0,250)
plt.xlim(0,122)
plt.savefig('./figure/line_area_01.png',dpi=200,bbox_inches='tight',pad_inches=0)
plt.show()
```


​    
![png](output_55_0.png)
​    

