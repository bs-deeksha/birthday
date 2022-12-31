import streamlit as st
import time
st.set_page_config(layout="wide")
st.markdown("<h2 style='text-align: center; color: black;'>Here's to 26 wonderful years  🥳 and 74 more 😜</h2>", unsafe_allow_html=True)

c1,c2,c3=st.columns([0.5,2,1])
with c2:
    ph1 = st.empty()
    ph2=st.empty()
    n= 27
    for i in range(1,n):
        if i%2==0:
            ph2.image('balloon1.png',width=500)
            ph1.markdown("<h3 style='text-align: center; color: black;'>"+str(i)+"</h3>", unsafe_allow_html=True)
        else:
            ph2.image('balloon2.png',width=500)
            ph1.markdown("<h3 style='text-align: center; color: black;'>"+str(i)+"</h3>", unsafe_allow_html=True)
        # time.sleep(0.1)
    st.balloons()
    ph2.image('birthday.jfif',width=1000)
    st.balloons()
    st.balloons()
    time.sleep(5)
