import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv(
    r"C:\Users\JeAdkins\OneDrive - CreditOne Bank\Documents\glucose.csv", dtype="unicode")



st.dataframe(df)
fig2a = px.line(x=df['Date'], y=df['Glucose Level'],
                    markers=True, title='Glucose Levels', labels={'y': 'GLucose', 'x': 'Date',})
st.plotly_chart(fig2a)