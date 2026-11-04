import streamlit as st
import pandas as pd

st.title("Stream Lit Text Input")

name = st.text_input("Enter Your Name")

if name:
    st.write(f"name {name}")

age = st.slider("Select your Age :", 0, 100, 25)

options = ["Python", "Java", "JavaScript", "C++"]
choice = st.selectbox("Choose your favorite Language :", options)
st.write(f"You Selected :{choice}")

st.write(f"Your Age :{age}")

import pandas as pd

df = pd.DataFrame(
    {
        "name": ["Arun", "Rahul", "Priya", "Sneha", "Kiran"],
        "age": [24, 27, 23, 25, 29],
        "city": ["Hyderabad", "Bangalore", "Chennai", "Mumbai", "Delhi"],
    }
)

st.write(df)


uploaded_file = st.file_uploader("Choose CSV file", type="csv")
if uploaded_file is not None:
    read_df = pd.read_csv(uploaded_file)
    st.write(read_df)
