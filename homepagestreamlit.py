import streamlit as st
from disease_data import Data
import charts
import pandas as pd
def homepage():
    df = pd.read_csv('Global Health Statistics.csv')
    st.write(df)
    chart1 = charts.bar_chart_population_affected(df)
    chart2 = charts.box_plot_treatment_cost(df)
    st.markdown("<br><br><br><br><br>", unsafe_allow_html=True)
    st.pyplot(chart1)
    st.markdown("<br><br><br><br><br>", unsafe_allow_html=True)
    st.pyplot(chart2)
  
