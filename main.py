import streamlit as st
from query import Query
from datetime import date, timedelta

# 设置应用程序的布局为wide mode
st.set_page_config(layout="wide")

# 实例化Query对象
query = Query()

today = date.today()

# 计算一个月前和一个月后的日期
one_month_ago = today - timedelta(days=30)
one_month_later = today + timedelta(days=30)


# 第一个查询表单
st.sidebar.subheader('突变日期查询')
date1 = st.sidebar.date_input('请选择日期', min_value=one_month_ago, max_value=one_month_later, value=today)
query_button1 = st.sidebar.button('查询', key='query1')

# 第二个查询表单
st.sidebar.subheader('突变出现日期查询')
map_location = st.sidebar.selectbox('选择地图', query.map_location)
game_mode = st.sidebar.selectbox('选择玩法', query.game_mode)
date2 = st.sidebar.date_input('选择日期', min_value=one_month_ago, max_value=one_month_later, value=today)
query_button2 = st.sidebar.button('查询', key='query2')

# 主页面内容
st.title('After the Fall 突变查询器')

col1, col2 = st.columns(2)

with col1:
    # 根据表单1的查询按钮点击状态执行查询
    if query_button1:
        result1 = query.query1(str(date1))
        st.write('突变日期查询表: ')
        print(result1)
        st.write(result1)

    # 根据表单2的查询按钮点击状态执行查询
    if query_button2:
        result2 = query.query2(map_location, game_mode, str(date2))
        st.write('突变出现日期查询表: ')
        st.write(result2)

with col2:
    st.write('After the Fall查询器使用说明：')
    st.write('1、“突变日期查询表”， 选择日期，再点击查询，可以查询当前到指定日期期间的突变')
    st.write('2、“突变出现日期查询表”，选择地图、玩法和日期，再点击查询，可以查询具体某个突变的出现日期。')
    st.write('数据提供: E-11')