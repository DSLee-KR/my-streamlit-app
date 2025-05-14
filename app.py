import streamlit as st

st.title("간단한 계산기")

num1 = st.number_input("첫 번째 숫자", value=0)
num2 = st.number_input("두 번째 숫자", value=0)

if st.button("더하기"):
    st.write("결과:", num1 + num2)
