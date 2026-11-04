import streamlit as st
import pandas as pd
import numpy as np

## Title of the application

st.title("Hello Streamlit")

# Display Simple Text
st.write("This is a Simple Text...")

df = pd.DataFrame({"first_column": [1, 2, 3, 4], "second_column": [10, 20, 30, 40]})
# Display the dataframe
st.write("Here Is the DataFrame.")
st.write(df)

# Create a Line Chart
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.line_chart(chart_data)
st.line_chart(df)
