import streamlit as st
from datetime import datetime
import time

st.title("Current Time App")

# Create a placeholder for the time
time_placeholder = st.empty()

# Create a loop that updates the time every second
while True:
    current_time = datetime.now().strftime("%H:%M:%S")
    time_placeholder.markdown(f"## The current time is: **{current_time}**")
    time.sleep(1)
