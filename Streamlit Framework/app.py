import streamlit as st
import pandas as pd
import numpy as np

# Title of page
st.title("Streamlit !!")

# Basic text
st.write("Hello world")

# Basic dataframe
data = [
    {"name": "Alice", "age": 25, "city": "New York"},
    {"name": "Bob", "age": 30, "city": "Los Angeles"},
    {"name": "Charlie", "age": 35, "city": "Chicago"},
]
df = pd.DataFrame(data)
st.write("here are users")
st.write(df)

# # Display chart for dataframe
# chart = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
# st.write(chart)
# st.line_chart(chart)

# Input
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello {name}")

age = st.slider("Age:", 0, 100, 18)
st.write(f"Your age: {age}")

options = ["python", "java", "c++"]
choice = st.selectbox(f"Choose language:", options)
st.write(f"Your language: {choice}")

uploaded_file = st.file_uploader("Choose csv file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
