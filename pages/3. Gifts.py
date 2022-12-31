import streamlit as st
import time
st.set_page_config(layout="wide")
st.title("Gift Time 🎁🎉!!")


category=st.selectbox("Choose a Category",["Chocolates","Cash"])
if category=='Chocolates':
    gift=st.radio("Which one among these?",["Ferrero Rocher","Kit Kat","Dairy Milk"],horizontal=True)
    col1,col2,col3=st.columns(3)
    with col1:
        st.image('ferrero.png',width=300)
    with col2:
        st.image('kitkat.png',width=300)
    with col3:
        st.image('dairymilk.png',width=300)
else:
    gift=st.radio("Which one among these? ",["501","1001"],horizontal=True)
    col1,col2,col3=st.columns(3)
    with col1:
        st.image('501.jpg',width=300)
    with col2:
        st.image('1001.jpg',width=300)
submitted = st.button("Add to cart")
if submitted:
    st.write("Your selection is "+category+" : "+gift)
    st.balloons()
    time.sleep(2)
    st.subheader("Woww! You chose my favourite 😍")
    st.balloons()
    time.sleep(2)
    st.subheader("Please send the selected gift to my address(refer Amazon) as a treat 💃!")
    time.sleep(1)
    st.subheader("Thanks in Advance ❤️! Sooo sweet of you😜")
