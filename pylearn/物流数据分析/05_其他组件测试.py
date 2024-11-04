#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :05_其他组件测试.py
# @Time      :2024/10/31 14:32
# @Author    :雨霓同学
# @Function  :
import streamlit as st
#
# # 反馈部件的使用
# sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
#
# select = st.feedback()  # 默认显示,点赞或点踩
# if select is not None:
#     st.write(f"你的选择是: {sentiment_mapping[select]}")
# # select = st.feedback(options='faces') # 显示一排表情符号
# select = st.feedback(options='stars')  # 显示一排星星
#
# st.write(select)
#
# # 表单控件和表单提交控件
# with st.form("my_form"):
#     name = st.text_input(label="请输入你的名字")
#     email = st.text_input(label="请输入你的邮箱")
#     submit = st.form_submit_button("提交按钮", icon=":material/send:")   # 表单提交按钮
#     if submit:
#         st.write(f"你的名字是:{name},你的邮箱是:{email}")
#
# # 开关组件
# notify_user = st.toggle("请阅读用户使用须知", value=False, help='点击此选项,表示你同意我们的使用须知')
#
# if notify_user:
#     st.write("你同意了使用须知")
# else:
#     st.write("你没有同意使用须知")
#
# # 日期输入控件
# import datetime
# import streamlit as st
#
# d = st.date_input("你的生日是什么时候？", datetime.date(1996, 1, 1),
#         format="YYYY-MM-DD"
#                 )
# st.write("你的生日是:", d)

# 数据编辑控件
import pandas as pd
from nltk import download
from streamlit import download_button
st.set_page_config(page_title="物流数据分析系统", page_icon=":memo:", layout="wide")  # 设置页面标题、图标和布局
data = pd.read_csv('./data/all_address_crood.csv', encoding='utf-8')
# st.dataframe(data)

# table = st.data_editor(data.head())
# st.dataframe(table)

# 要求用户可以上传文件file_uploader

import streamlit as st
import os
import sweetviz as sv
from streamlit.components.v1 import html
# 添加自定义 CSS 来指定页面宽度
custom_css = """
    <style>
    .stApp {
        width: 1100px !important;
        
        margin: auto;
    }
    </style>
"""

# 将自定义 CSS 插入到页面头部
st.markdown(custom_css, unsafe_allow_html=True)


uploaded_file = st.file_uploader(
    "你可以选择性上传一个CSV文件",
    type=['csv'],
    accept_multiple_files=False
)

left,middle, right = st.columns(3,gap='large')

if left.button("点击查看文件"):
    if uploaded_file is not None:
        st.success('文件已上传成功!文件内容如下:', icon="✅")
        data = pd.read_csv(uploaded_file, encoding='utf-8')
        st.dataframe(data)
    else:
        st.error("你没有上传任何文件", icon="🚨")

# 检测用户之前生成的报告是否存在,如果存在则删除
if os.path.exists('report.html'):
    os.remove('report.html')


# 初始化Streamlit会话状态
if 'report_generated' not in st.session_state:   # 生产报告
    st.session_state['report_generated'] = False
if 'report_content' not in st.session_state:  # 报告内容
    st.session_state['report_content'] = None

# 显示生成报告的按钮
generate_report_button = middle.button('生成数据报告')

# 如果用户点击了生成报告按钮，并且有上传的文件
if generate_report_button and uploaded_file is not None:
    data = pd.read_csv(uploaded_file, encoding='utf-8')
    report = sv.analyze(data)
    report.show_html('report.html', open_browser=False, layout='vertical', scale=1.0)
    with open('report.html', 'r', encoding='utf-8') as f:
        st.session_state['report_content'] = f.read()
    st.session_state['report_generated'] = True
elif generate_report_button:
    st.error('请先上传文件，然后再点击生成数据分析报告按钮。')
# 显示报告
if generate_report_button:
    if st.session_state['report_generated'] and st.session_state['report_content'] is not None:
        st.success('数据分析报告已生成!具体内容如下:')
        st.success('数据分析报告已生成!,可以点击下载')
        html(st.session_state['report_content'], scrolling=True, width=934, height=600,)



# 显示下载报告的按钮

# download_report_button = right.button('下载数据报告')
#
# # 如果用户点击了下载报告按钮，检查报告是否已经生成
# if download_report_button and st.session_state['report_generated']:
#     st.success('数据分析报告渲染中,请再次点击下载!')
#     download = st.download_button(
#         label='下载数据报告',
#         use_container_width=True,
#         data=st.session_state['report_content'].encode('utf-8'),
#         file_name='data_analysis_report.html',
#     )
# elif download_report_button and not st.session_state['report_generated']:
#     # 如果未生成，提示用户先生成报告
#     st.error('报告尚未生成，请先点击“生成数据分析报告”按钮。')
# 修改版:

if st.session_state['report_generated']:
    button_right = right.download_button(
        label='下载数据报告',
        use_container_width=True,
        data=st.session_state['report_content'].encode('utf-8'),
        file_name='data_analysis_report.html',
    )
    
    if button_right:
        st.info('数据分析报告下载完成!欢迎再次使用')




# if st.button('点击查看数据分析报告'):
#     if uploaded_file is not None:
#         data = pd.read_csv(uploaded_file, encoding='utf-8')
#         report = sv.analyze(data)
#         report.show_html('report.html', open_browser=False, layout='vertical', scale=1.0)
#         with open('report.html', 'r', encoding='utf-8') as f:
#             data = f.read()
#         html(data, height=1000, width=1200,scrolling=True,)
# if os.path.exists('report.html'):
#     st.download_button(label='下载数据分析报告',
#         data=open('report.html', 'rb'),
#         file_name='data_analysis_report.html')


if __name__ == "__main__":
    run_code = 0
