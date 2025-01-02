import streamlit as st
import homepagestreamlit

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




"""
python -m streamlit run "d:/Semester 5/Intro to Data Science/Data Science Project/streamlitt.py"

"""

