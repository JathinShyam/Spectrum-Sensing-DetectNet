import streamlit as st
from PIL import Image
import pandas as pd

st.title("Models")


option = st.selectbox(
    'Select the model',
    ('CNN', 'CLDNN', 'LSTM', 'DNN'))

if option=='CNN':
    img = Image.open("cnnmodel.jpg")
    st.image(img)

    data = {'Hyperparameter': ['Filters per Conv layer', 'Filter size', 'Cells per CNN layer', 
                               'Neurons per FC layer', 'Optimizer', 'initial learning rate',
                               'Batch size', 'Dropout ratio'],
            'Value': [60,3,256,128,'Adam',0.0003,200,0.2]}

    df = pd.DataFrame(data)
    st.table(df)
    
elif option=='CLDNN':
    img = Image.open("cldnnmodel.jpg")
    st.image(img)

    data = {'Hyperparameter': ['Filters per Conv layer', 'Filter size', 'Cells per CNN layer', 
                               'Neurons per FC layer', 'Optimizer', 'initial learning rate',
                               'Batch size', 'Dropout ratio'],
            'Value': [60,3,60,128,'Adam',0.0003,200,0.3]}

    df = pd.DataFrame(data)
    st.table(df)

elif option=='LSTM':
    img = Image.open("lstmmodel.jpg")
    st.image(img)

    data = {'Hyperparameter': ['Filters per Conv layer', 'Filter size', 'Cells per CNN layer', 
                               'Neurons per FC layer', 'Optimizer', 'initial learning rate',
                               'Batch size', 'Dropout ratio'],
            'Value': [60,3,300,128,'Adam',0.0003,200,0.3]}

    df = pd.DataFrame(data)
    st.table(df)

elif option=='DNN':
    img = Image.open("dnnmodel.jpg")
    st.image(img)

    data = {'Hyperparameter': ['Filters per Conv layer', 'Filter size', 'Cells per CNN layer', 
                               'Neurons per FC layer', 'Optimizer', 'initial learning rate',
                               'Batch size', 'Dropout ratio'],
            'Value': [60,3,512,128,'Adam',0.0003,200,0.2]}

    df = pd.DataFrame(data)
    st.table(df)