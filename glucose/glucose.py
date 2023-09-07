import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv(
    r"C:\Users\JeAdkins\OneDrive - CreditOne Bank\Documents\glucose.csv", dtype="unicode")
df2 = pd.read_csv(
    r"C:\Users\JeAdkins\OneDrive - CreditOne Bank\Documents\gl.csv", dtype="unicode")

st.sidebar.header('Navigation')
page_names = ['Home', "1 Month Graph", "Epilogue", "About"]
page = st.sidebar.radio("", page_names, index=0, key="nav")

graph_options = ['All', "Morning", "Noon", "Night"]


st.title("Glucose Level Dashboard")
if page == "Home":

    st.write('hi')

elif page == "1 Month Graph":

    st.subheader('Glucose Levels from June 20 - May 20')
    st.dataframe(df, width=800)

    to_plot = [v for v in list(df.columns) if v.startswith('Glucose')]
    fig1 = px.line(df, x=df['Date'], y=to_plot)
    st.plotly_chart(fig1)

    st.write('stuff here!!! ')


elif page == "Epilogue":
    st.write('everything else')
    st.dataframe(df2, width=800)


elif page == "About":
    st.write('resources')
