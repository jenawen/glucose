import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import math
from datetime import date, datetime

df = pd.read_csv(
    r"C:\Users\JeAdkins\OneDrive - CreditOne Bank\Documents\glucose.csv", dtype="unicode")

df2 = pd.read_csv(
    r"C:\Users\JeAdkins\OneDrive - CreditOne Bank\Documents\gl.csv", dtype="unicode")

st.sidebar.header('Navigation')
page_names = ['Home', "1 Month Graph", "Epilogue", "Resources", ]
page = st.sidebar.radio("", page_names, index=0, key="nav")

graph_options = ['All', "Morning", "Noon", "Night"]


st.title("Glucose Level Dashboard")
if page == "Home":

    st.subheader('Background')
    st.write('Around early 2023, my boyfriend started feeling bad, as in he always felt sluggish, tired, and achey.')
    st.subheader('Data Collection')
    st.write('To take his glucose readings, we use a standard glucose monitor and test strips. For the first month, we took three readings a day: in morning, afternoon, and at night. Times for data collection were arbitrary, but we often followed the routine of taking a reading right after waking up, after lunch, and right before bed. ')


elif page == "1 Month Graph":

    to_plot = [v for v in list(df.columns) if v.startswith('Glucose')]
    fig1 = px.line(df, x=df['Date'], y=to_plot,
                   title='AM, Noon, and PM Readings')
    st.plotly_chart(fig1)
    st.write('For a month, we took three blood sugar readings a day. His sugar levels dropped quite dramatically in the first couple of days. We cut out sugary drinks and foods immediately. We tried eating more lean and whole foods, which also helped lower his blood sugar levels.')
    st.write('His doctor was concerned that at his levels from his most recent blood test that he was already extremely diabetic, and wanted to put him on insulin right away. However, we opted for the less scary and expensive medication Metformin, which also helped lower his glucose levels a lot.')
    st.write('We paid more attention to his morning readings than the noon and night ones. This is because his blood sugar level in the morning after waking up is also known as his fasting glucose level, which is used as an indicator for diabetes.')
    st.divider()

    c1, c2, c3 = st.columns(3)
    am_list = df['Glucose AM'].astype(int)
    n_list = df['Glucose Noon'].replace(
        to_replace='None', value=np.nan).dropna().astype(int)
    pm_list = df['Glucose PM'].astype(int)

    with c1:
        st.subheader('AM Stats')
        st.write(f'**Average:** {math.trunc(am_list.sum() / (len(df) - 1))}')
        st.write(f'**Maximum:** {max(am_list)}')
        st.write(f'**Minimum:** {min(am_list)}')

    with c2:
        st.subheader('Noon Stats')
        st.write(
            f'**Average:** :red[{math.trunc(n_list.sum() / (len(df) - 1))}*]')
        st.write(f'**Maximum:** {max(n_list)}')
        st.write(f'**Minimum:** {min(n_list)}')

    with c3:
        st.subheader('PM Stats')
        st.write(f'**Average:** {math.trunc(pm_list.sum() / (len(df) - 1))}')
        st.write(f'**Maximum:** {max(pm_list)}')
        st.write(f'**Minimum:** {min(pm_list)}')

    st.caption('*The data set for Noon values is incomplete, therefore the average for Noon readings may or may not be totally accurate.')

    t1, t2, t3 = st.tabs(['AM', "Noon", "PM"])

    with t1:
        am_df = pd.DataFrame({'y': [min(am_list), max(am_list), math.trunc(
            am_list.sum() / (len(df) - 1))], "x": ["Min", "Max", "Avg"]})
        am_fig = px.scatter(am_df, x=am_df['x'], y=am_df['y'], )
        st.plotly_chart(am_fig)
    with t2:
        n_df = pd.DataFrame({'y': [min(n_list), max(n_list), math.trunc(
            n_list.sum() / (len(df) - 1))], "x": ["Min", "Max", "Avg"]})
        n_fig = px.scatter(n_df, x=n_df['x'], y=n_df['y'])
        st.plotly_chart(n_fig)
    with t3:
        pm_df = pd.DataFrame({'y': [min(pm_list), max(pm_list), math.trunc(
            pm_list.sum() / (len(df) - 1))], "x": ["Min", "Max", "Avg"]})
        pm_fig = px.scatter(pm_df, x=pm_df['x'], y=pm_df['y'])
        st.plotly_chart(pm_fig)

    st.divider()

    dateDf = pd.to_datetime(df['Date'], format='%m/%d/%Y')
    minDate = dateDf.min().date()
    maxDate = dateDf.max().date()

    st.subheader(f'Overall Glucose Values from {minDate} to {maxDate}')
    st.dataframe(df, width=800)

elif page == "Epilogue":
    glucose_list = df2['Glucose'].replace(
        to_replace='None', value=np.nan).dropna().astype(int)
    g_sum = glucose_list.sum()
    num_of_v = len(df2) - 1

    fig1 = px.line(df2, x=df2['Date'], y=df2['Glucose'],
                   title="Glucose levels from June to Sept")
    st.plotly_chart(fig1)
    st.write('After his second doctor visit, we kept monitoring his glucose levels daily. We tried cutting out more sugar, but he had a small treat every once in a while. ')
    st.divider()

    c1, c2, c3 = st.columns(3)
    with c1:
        st.subheader('Average')
        st.write(f'{math.trunc(g_sum / num_of_v)}')
    with c2:
        st.subheader('Maximum')
        st.write(f'{max(glucose_list)}')
    with c3:
        st.subheader('Minimum')
        st.write(f'{min(glucose_list)}')

    st.divider()

    st.subheader('Add a New Reading')
    with st.form('my_form'):
        st.date_input(label="Select a Date", format="MM/DD/YYYY")
        st.time_input(label="Input a Time")
        st.number_input(label="Input a Number", min_value=0)
        st.text_input(label="Password")
        st.form_submit_button(label="Submit")
    st.subheader('Overall Glucose Values')
    st.dataframe(df2.dropna(how='all'), width=800)

    datetime.now().date()

elif page == "Resources":
    st.subheader('Helpful Links')
    st.write('link here')
    st.write('another link here')
