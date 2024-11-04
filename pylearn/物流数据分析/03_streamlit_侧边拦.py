#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :03_streamlit_侧边拦.py
# @Time      :2024/10/30 16:56
# @Author    :雨霓同学
# @Function  :

import streamlit as st
import pandas as pd

st.sidebar.title('☘ 物流数据分析 ☘')
st.sidebar.text('这个是物流数据分析的控制面板')

username = st.sidebar.text_input('用户名', '请输入用户名')
st.sidebar.text('可以让用户输入自己的名称')

data_name = st.sidebar.text_input('省份名称', placeholder="请输入你要查询的省份",)


if data_name == '':
    pass
else:
    data = pd.read_excel(f'data/{data_name}.xls', nrows=10)
    st.write(f'{data_name}的数据如下所示:')
    st.dataframe(data)

age = st.sidebar.number_input('请输入你的年龄', min_value=0, max_value=100)
st.write(f'你输入的年龄是: {age}')

city_name = st.sidebar.selectbox('请输入你要查询的城市',['湖南','湖北'], placeholder='请输入你要查询的城市',
                                index=None)

if city_name == None:
    pass
else:
    data = pd.read_excel(f'data/{city_name}.xls', nrows=10, usecols=range(5))
    st.write(f'你选择的城市是: {city_name}')
    st.dataframe(data)

city = st.sidebar.radio('你要查询的城市是:',['选项A \t 武汉','选项B\t襄阳','选项C\t长沙'] ,
                        index=None,
                        horizontal=True
                        )
st.write(f'你选择的城市是: {city}')

options = st.sidebar.multiselect('请输入你要选择的内容: ',
                    ['长沙','武汉','襄阳']
                    )
st.write(f'你选择的内容是: {options}')

checked = st.sidebar.checkbox('是否开启订阅',value=True, help='勾选此项表示你将会获得订阅')
if checked:
    st.write('你开启了订阅')
else:
    st.write('你关闭了订阅')


if __name__ == "__main__":
    run_code = 0
