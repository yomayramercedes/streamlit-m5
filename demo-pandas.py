# import streamlit
import streamlit as st 
import pandas as pd 

names_link = 'dataset.csv'
# read csv
names_data = pd.read_csv(names_link)

# create title
st.title ('Pandas dataframe')

# print dataframe
st.dataframe(names_data)
