import streamlit as st
import time
st.set_page_config(layout="wide")

st.title("Make a Wish")

wish=st.text_input("Make a wish here")
done=st.button("Done")
if done:
    if wish:
        st.subheader("Tathasthu! Consider it done :)")
        st.image('hanuma.jfif',width=500)
    else:
        st.warning("U gotta wish something!")
