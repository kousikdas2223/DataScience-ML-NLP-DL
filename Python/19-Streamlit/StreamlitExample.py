import streamlit as streamlit
import pandas as pd
import numpy as np

# Initialize Streamlit app

streamlit.title('Data Analysis Dashboard')

streamlit.write('This is a header')

# Load the data

data = pd.read_csv('salesData.csv')

# Display the first few rows

streamlit.dataframe(data, width=10000)

# Perform some basic analysis

streamlit.write('Mean:', np.mean(data['Total Revenue']))

streamlit.write('Median:', np.median(data['Total Revenue']))

streamlit.write('Mode:', data['Total Revenue'].mode())

streamlit.write('Standard Deviation:', np.std(data['Total Revenue']))

streamlit.write('Variance:', np.var(data['Total Revenue']))

# Create a chart

streamlit.bar_chart(data['Total Revenue'])

streamlit.line_chart([data['Total Revenue'], data['Sale Price']])

streamlit.area_chart(data['Total Revenue'])

name= streamlit.text_input("Enter your name: ")
age = streamlit.slider("Select your age", 0,100,25)
if name and age:
    streamlit.write(f"Hello, {name}!")
    streamlit.write(f"You are {age} years old.")

options = ["Python", "JavaScript", "Java", "Oracle"]
choice = streamlit.selectbox("Choose your options", options)

if choice:
    streamlit.write(f"You selected: {choice}")
    streamlit.balloons()

uploaded_file = streamlit.file_uploader("Choose a file to upload", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    streamlit.write(df)
    streamlit.write(f"Mean: {np.mean(df['Total Revenue'])}")
    streamlit.write(f"Median: {np.median(df['Total Revenue'])}")
    streamlit.bar_chart(df['Total Revenue'])
    streamlit.line_chart([df['Total Revenue'], df['Sale Price']])
    