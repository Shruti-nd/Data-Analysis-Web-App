import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np 

st.title("DATA ANALYSIS")
st.subheader("Data Analysis using Python and Streamlit")

upload= st.file_uploader("Upload your dataset(IN CSV format)")
if upload is not None:
    data=pd.read_csv(upload)

if upload is not None:
    if st.checkbox("Preview Dataset"):
        if st.button("Head"):
            st.write(data.head(10))
        if st.button("Tail"):
            st.write(data.tail(10))

if upload is not None:
    if st.checkbox("Data type of each column"):
        st.text("Data Types")
        st.write(data.dtypes)

if upload is not None:
    data_shape=st.radio("What dimension do you want to check?",('Rows','Columns'))
    if data_shape=='Rows':
        st.text("Number of rows: ")
        st.write(data.shape[0])
    if data_shape=='Columns':
        st.text("Number of columns: ")
        st.write(data.shape[1])

if upload is not None:
    test=data.isnull().values.any()
    if test==True:
        if st.checkbox("Null values in the dataset"):
            sns.heatmap(data.isnull())
            st.pyplot()
    else:
            st.success("Congratulations!! No missing values")

if upload is not None:
    test= data.duplicated().any()
    if test==True:
        st.warning("This dataset contains some duplicate values")
        dup=st.selectbox("Do you want to remove duplicate values?"),("Select one","Yes","No")
        if dup=="Yes":
            data.drop.duplicates()
            st.text("Duplicate values are removed")
        if dup=="No":
            st.text("Ok, No Problem")
    
if upload is not None:
    if st.checkbox("Summary of Dataset"):
        st.write(data.describe(include='all'))

if st.button("About App"):
    st.text("Built with Streamlit")

if st.checkbox("By"):
    st.success("Shruti Jain")