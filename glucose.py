import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import math
from datetime import date, datetime

st.set_page_config(layout='wide')

df = pd.read_csv(
    r"U:\repo\glucose\glucose.csv", dtype="unicode")

df2 = pd.read_csv(
    r"U:\repo\glucose\gl.csv", dtype="unicode")

st.sidebar.header('Navigation')
page_names = ['Home', "1 Month Graph", "Epilogue", "Resources", ]
page = st.sidebar.radio("", page_names, index=0, key="nav")

graph_options = ['All', "Morning", "Noon", "Night"]

st.title("Glucose Level Dashboard")
if page == "Home":
    st.subheader('Background')
    st.write('Around early 2023, my boyfriend started feeling bad. He always felt sluggish, tired, and achey.')
    st.subheader('Data Collection')
    st.write('To take his glucose readings, we use a standard glucose monitor and test strips. For the first month, we took three readings a day: in morning, afternoon, and at night. Times for data collection were arbitrary, but we often followed the routine of taking a reading right after waking up, after lunch, and right before bed. ')
    st.write('His first reading was usually taken before eating anything, while his afternoon and night readings where taken a few hours after eating. His morning, or fasting, readings were considered the most reflective of how his body was processing sugar. ')

elif page == "1 Month Graph":
    to_plot = [v for v in list(df.columns) if v.startswith('Glucose')]
    fig1 = px.line(df, x=df['Date'], y=to_plot,
                   title='AM, Noon, and PM Readings', height=550)
    st.plotly_chart(fig1, use_container_width=True)
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

    # t1, t2, t3 = st.tabs(['AM', "Noon", "PM"])

    # with t1:
    #     am_df = pd.DataFrame({'y': [min(am_list), max(am_list), math.trunc(am_list.sum() / (len(df) - 1))], "x": ["Min", "Max", "Avg"]})
    #     am_fig = px.scatter(am_df, x=am_df['x'], y=am_df['y'], color=am_df['x'])
    #     st.plotly_chart(am_fig)
    # with t2:
    #     n_df = pd.DataFrame({'y': [min(n_list), max(n_list), math.trunc(n_list.sum() / (len(df) - 1))], "x": ["Min", "Max", "Avg"]})
    #     n_fig = px.scatter(n_df, x=n_df['x'], y=n_df['y'])
    #     st.plotly_chart(n_fig)
    # with t3:
    #     pm_df = pd.DataFrame({'y': [min(pm_list), max(pm_list), math.trunc(pm_list.sum() / (len(df) - 1))], "x": ["Min", "Max", "Avg"]})
    #     pm_fig = px.scatter(pm_df, x=pm_df['x'], y=pm_df['y'] )
    #     st.plotly_chart(pm_fig)
    st.divider()
    # dateDf = pd.to_datetime(df['Date'], format='%m/%d/%Y')
    # minDate = dateDf.min().date()
    # maxDate = dateDf.max().date()
    st.subheader(f'Overall Glucose Values')
    st.dataframe(df.dropna(how='all'), use_container_width=True)

elif page == "Epilogue":

    if 'def_df' not in st.session_state:
        st.session_state['def_df'] = df2

    def add_new_reading():
        if submit:
            # need to format date and time
            new_df = pd.DataFrame(
                {'Date': date, 'Time (AM)': time, 'Glucose': num}, index=[0])
            st.session_state['def_df'] = pd.concat(
                [st.session_state['def_df'], new_df], axis=0)
            st.dataframe(st.session_state['def_df'].replace(
                np.nan, 'None'), width=800)

    glucose_list = df2['Glucose'].replace(
        to_replace='None', value=np.nan).dropna().astype(int)
    g_sum = glucose_list.sum()
    num_of_v = len(df2) - 1

    fig1 = px.line(df2, x=df2['Date'], y=df2['Glucose'],
                   title="Glucose levels from June to Sept", height=550)
    st.plotly_chart(fig1, use_container_width=True)
    st.write('After his second doctor visit, we kept monitoring his glucose levels daily. We tried cutting out more sugar, but he had a small treat every once in a while. We switched to diet and zero sugar drinks and juices, because I did not want to completely cut out something he enjoyed.')
    st.write('I wanted to focus on a high fiber and high protein diet. We tried to cut out added sugars and high carbohydrate foods from our daily diet and only had them in moderation.')
    st.write('Exercise was also emphasized, but mostly light cardio and walking. Light exercise was beneficial not only to keep his glucose levels low, but also for his cardiovascular health.')
    st.write('After his third doctor visit and follow-up, we got some really great news. As of October 2023, his A1C levels dropped by almost half and the rest of his blood test results suggest that he is not even in prediabetic ranges anymore. If he keeps up his progress, he may not even need to take medicine in the future. She also put him on a lower dose of Metformin. ')

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
        date = st.date_input(label="Select a Date", format="MM/DD/YYYY")
        time = st.time_input(label="Input a Time")
        num = st.number_input(label="Input a Number", min_value=0)
        pw = st.text_input(label="Password")
        submit = st.form_submit_button(
            label="Submit", on_click=add_new_reading)

    st.subheader('Overall Glucose Values')
    st.dataframe(df2.dropna(how='all'), use_container_width=True)

    datetime.now().date()

    if __name__ == "__add_new_reading__":
        add_new_reading()

elif page == "Resources":
    st.subheader('Helpful Links')

    st.write('link here')
    st.write('another link here')
