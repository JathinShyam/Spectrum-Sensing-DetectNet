import streamlit as st
from PIL import Image

st.title("Results")

option = st.selectbox(
    'Select the model',
    ('CNN', 'CLDNN', 'LSTM', 'DNN'))

if option=='CNN':
    img = Image.open("CNN.jpg")
    st.image(img)
elif option=='CLDNN':
    img = Image.open("CLDNN.jpg")
    st.image(img)
elif option=='LSTM':
    img = Image.open("lstm.jpg")
    st.image(img)
elif option=='DNN':
    img = Image.open("dnn.jpg")
    st.image(img)