import streamlit as st
from PIL import Image


st.title("Spectrum Sensing in Cognitive Radio using DetectNet")
st.sidebar.success("Select a page above.")



col1, col2 = st.columns(2)

with col1:
   st.subheader("Team Members")
   st.markdown("**Balashanmugam M**")
   st.text("124156028")
   st.markdown("**Shyam Kumar Reddy K**")
   st.text("124156048")

with col2:
   st.subheader("Guide")
   st.markdown("**Kannan K**")
   st.text("Professor")
   st.text("School of Computing")


st.subheader("Paper deatils")
st.markdown("**Deep Learning for Spectrum Sensing**")

st.text("IEEE WIRELESS COMMUNICATIONS LETTERS, VOL. 8, NO. 6, DECEMBER 2019")
st.text("Jiabao Gao, Xuemei Yi, Caijun Zhong , Xiaoming Chen , and Zhaoyang Zhang")

st.write("check out this [IEEE](https://ieeexplore.ieee.org/document/8824091)")
