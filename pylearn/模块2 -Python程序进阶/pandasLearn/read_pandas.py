
import pandas as pd
import numpy as np

data = pd.read_csv("beijing_tianqi_2018.csv")
print(data.head())
#通过列名来获取元素
#print(data["tianqi"])
#print(data[["tianqi","aqi"]])

# print(data.loc[:4,"fengli":])
# print(data.loc[:4,["fengli","aqi","aqiInfo","aqiLevel"]])
# print(data.loc[[0,1,2],["fengli","aqi"]])
print(data)
# #查询第十行第七列
# print(data.iloc[9,6])
# #查询所有偶数行偶数列
# print(data.iloc[::2,::2])
print(data[data["aqi"]>100])
print(data.loc[data["aqi"]>100])
print(data[(data['fengli']=='南风')&(data['aqi']>100)])