import streamlit as st
import homepagestreamlit
import charts
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Global Health Statistics.csv")

page = st.sidebar.selectbox("Choose a page", ["Home", "Page 1", "Page 2", "Page 3"])
st.title("Global Health Statistics")
if page == "Home":
    homepagestreamlit.homepage()
elif page == "Page 1":
    import pages.page_1
elif page == "Page 2":
    import pages.page_2
elif page == "Page 3":
    import pages.page_3

chart_option = st.selectbox("Select a chart to display:", [
    "Bar Chart: Population Affected",
    "Box Plot: Treatment Cost",
    "Histogram: Mortality Rate",
    "Scater: population_vs_recovery",
    "line: healthcare_access",
    "heatmap: correlation",
    "stacked_bar: gender_population",
    "violin_plot: dalys",
    "bubble_chart: hospital_beds_vs_healthcare"
    ""
])

if chart_option == "Bar Chart: Population Affected":
    st.pyplot(charts.bar_chart_population_affected(df))
elif chart_option == "Box Plot: Treatment Cost":
    st.pyplot(charts.box_plot_treatment_cost(df))
elif chart_option == "Histogram: Mortality Rate":
    st.pyplot(charts.histogram_mortality_rate(df))
elif chart_option == "Scater: population_vs_recovery":
    st.pyplot(charts.scatter_population_vs_recovery(df))
elif chart_option == "line: healthcare_access":
    st.pyplot(charts.line_chart_healthcare_access(df))
elif chart_option == "heatmap: correlation":
    st.pyplot(charts.heatmap_correlation(df))
elif chart_option == "stacked_bar: gender_population":
    st.pyplot(charts.stacked_bar_gender_population(df))
elif chart_option == "violin_plot: dalys":
    st.pyplot(charts.violin_plot_dalys(df))
elif chart_option == "bubble_chart: hospital_beds_vs_healthcare":
    st.pyplot(charts.bubble_chart_hospital_beds_vs_healthcare(df))






"""
python -m streamlit run "d:/Semester 5/Intro to Data Science/IDS Project/streamlitt.py"

"""

