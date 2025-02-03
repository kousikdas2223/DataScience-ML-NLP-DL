import streamlit as streamlit
import pandas as pd
import numpy as np

# Initialize Streamlit app

streamlit.title('Data Analysis Dashboard')

streamlit.write('This is a header')

# Create a list of discrete numerical data distribution

continuous_data = np.random.normal(loc=50, scale=10, size=1000)
discrete_data = np.random.normal(loc=50, scale=10, size=1000)

# Calculate the mean, median, mode, variance and standard deviation of continuous_data and discrete_data

mean_continuous = np.mean(continuous_data)
median_continuous = np.median(continuous_data)
mode_continuous = np.mode(continuous_data)[0][0]
variance_continuous = np.var(continuous_data)
std_continuous = np.std(continuous_data)

mean_discrete = np.mean(discrete_data)

# Display the calculated statistics

streamlit.write(f'Mean of Continuous Data: {mean_continuous}')
streamlit.write(f'Median of Continuous Data: {median_continuous}')
streamlit.write(f'Mode of Continuous Data: {mode_continuous}')
streamlit.write(f'Variance of Continuous Data: {variance_continuous}')
streamlit.write(f'Standard Deviation of Continuous Data: {std_continuous}')

streamlit.write(f'Mean of Discrete Data: {mean_discrete}')

