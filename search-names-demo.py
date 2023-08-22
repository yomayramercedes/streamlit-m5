import streamlit as st 
import pandas as pd 

st.title('Streamlit - Search names') 
DATA_URL = 'dataset.csv'

@st.cache
def load_data_byname(name):
    # read all dataset
    data = pd.read_csv(DATA_URL)
    # create dataframe 
    filtered_data_byname = data[data['name'].str.contains(name)]
    # return dataframe
    return filtered_data_byname

myname = st.text_input('Name :')

if (myname):
    # create filterbyname dataframe
    filterbyname = load_data_byname(myname)
    # count rows number 
    count_row = filterbyname.shape[0]

    st.write(f"Total names : {count_row}")

    st.dataframe(filterbyname)