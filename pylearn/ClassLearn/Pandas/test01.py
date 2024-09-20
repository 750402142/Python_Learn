import pandas as pd
import numpy as np

mylist = list('abcdef')   # 列表作为索引
myarr = np.random.randint(12,size=6)
s = pd.Series(data=myarr,index=mylist)
print(s)

data = pd.read_csv('"C:/Users/wang/Desktop/pyLearn/模块2 -Python程序进阶/beijing_tianqi_2018.csv"')
print(data.head())
