import streamlit as st
import pandas as pd

from datetime import time, datetime

from adodbapi.apibase import pythonTimeConverter
from streamlit_option_menu import option_menu
st.markdown('# 1.这是streamlit使用的测试')
st.write('## 1.1. hello')
# 可以用来写代码块
st.code('''
from adodbapi.apibase import pythonTimeConverter
from streamlit_option_menu import option_menu
''')
if __name__ == '__main__':
    run_code = 0


