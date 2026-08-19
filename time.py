import streamlit as st
from datetime import datetime

st.title("Current Time App")


@st.fragment(run_every="1s")
def show_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    st.markdown(f"## The current time is: **{current_time}**")


show_time()
