import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

# Page setup
st.set_page_config(
    page_title="Current Time",
    page_icon="🕐",
    layout="centered"
)

# New Jersey / Eastern Time
TIMEZONE = ZoneInfo("America/New_York")


# Custom CSS
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
}

.clock-container {
    background: rgba(15, 23, 42, 0.9);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 25px;
    padding: 45px 30px;
    text-align: center;
    max-width: 700px;
    margin: 50px auto;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.4);
}

.location {
    font-size: 22px;
    color: #cbd5e1;
    margin-bottom: 20px;
}

.time {
    font-family: monospace;
    font-size: 72px;
    font-weight: bold;
    color: #ffffff;
    letter-spacing: 5px;
    margin: 10px 0;
}

.ampm {
    font-size: 25px;
    color: #94a3b8;
    margin-bottom: 25px;
}

.day {
    font-size: 30px;
    font-weight: 600;
    color: #e2e8f0;
}

.date {
    font-size: 21px;
    color: #94a3b8;
    margin-top: 8px;
}

.timezone {
    font-size: 16px;
    color: #64748b;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)


# Create clock area
clock_placeholder = st.empty()


@st.fragment(run_every="1s")
def show_clock():

    now = datetime.now(TIMEZONE)

    time_string = now.strftime("%I:%M:%S")
    am_pm = now.strftime("%p")

    day_string = now.strftime("%A")
    date_string = now.strftime("%B %d, %Y")

    timezone_name = now.tzname()

    clock_placeholder.markdown(
        f"""
        <div class="clock-container">

            <div class="location">
                📍 Princeton Junction, New Jersey
            </div>

            <div class="time">
                {time_string}
            </div>

            <div class="ampm">
                {am_pm}
            </div>

            <div class="day">
                {day_string}
            </div>

            <div class="date">
                {date_string}
            </div>

            <div class="timezone">
                Eastern Time — {timezone_name}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


show_clock()
