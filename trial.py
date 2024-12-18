import streamlit as st

name=st.text_input("输入名字")
age=st.slider("请选择你的年龄",0,100,25)

st.write(f'你好,{name}!你的年龄是{age}岁。')