import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    layout='wide',
    page_icon=':bar_chart:',
    page_title='Dasboard',
    initial_sidebar_state='collapsed'
)

df = pd.read_csv('iris.csv')

st.plotly_chart(
    px.scatter(
        data_frame=df,
        x='sepal_length',
        y='sepal_width',
        color='species'
    ), use_container_width=True
)

st.plotly_chart(
    px.histogram(
        data_frame=df,
        x='sepal_length',
        # y='sepal_width',
        text_auto=True,
        nbins=30,
        color='species'
    ), use_container_width=True
)

st.plotly_chart(
    px.histogram(
        data_frame=df,
        x='sepal_length',
        # y='sepal_width',
        text_auto=True,
        nbins=30,
        color='species',
        cumulative=True
    ), use_container_width=True
)
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(
        px.pie(
            data_frame=df,
            names='species'
        ), use_container_width=True
    )

with col2:
    st.plotly_chart(
        px.pie(
            data_frame=df,
            names='species'
        ), use_container_width=True
    )    
st.table(
    df.describe()
)