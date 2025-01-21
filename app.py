import streamlit as st
import pandas as pd
import plotly_express as px
import numpy as np

vehicles_df = pd.read_csv('vehicles_us.csv')

vehicles_df['date_posted']= pd.to_datetime(vehicles_df['date_posted'], format= '%Y-%m-%d')
vehicles_df['model_year'] = vehicles_df['model_year'].fillna(vehicles_df['model_year'].mean())
vehicles_df['manufacturer'] = vehicles_df['model'].apply(lambda x: x.split()[0])
bins = [0, 5000, 10000, 15000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, np.inf]
labels = ['0-5k', '5k-10k', '10k-15k', '15k-20k', '20k-30k', '30k-40k', '40k-50k', '50k-60k', '60k-70k', '70k-80k', '80k-90k', '90k-100k', '100k+']
vehicles_df['price_range'] = pd.cut(vehicles_df['price'], bins=bins, labels=labels, right=False)

st.header('Data Viewer')
st.dataframe(vehicles_df)

st.header('Number of Vehicles by Price and Type')
fig1 = px.histogram(vehicles_df, x='type', color='price_range')
st.write(fig1)
