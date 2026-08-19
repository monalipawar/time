import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

st.set_page_config(
    page_title="Current Time",
    page_icon="🕐",
    layout="centered"
)

TIMEZONE = ZoneInfo("America/New_York")

# CSS
st.markdown("""
<style>
.clock-container {
    background: linear-gradient(135deg, #111827, #1e293b);
    border-radius: 30px;
    padding: 45px 30px;
    text-align: center;
    margin: 40px auto;
    max-width: 700px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.4);
}

.location {
    font-size: 22px;
    color: #cbd5e1;
    margin-bottom: 25px;
}

.time {
    font-family: monospace;
    font-size: 75px;
    font-weight: bold;
    color: white;
    letter-spacing: 4px;
}

.ampm {
    font-size: 25px;
    color: #94a3b8;
    margin-top: 5px;
}

.day {
    font-size: 30px;
    font-weight: bold;
    color: white;
    margin-top: 25px;
}

.date {
    font-size: 20px;
    color: #cbd5e1;
    margin-top: 8px;
}

.timezone {
    font-size: 15px;
    color: #64748b;
    margin-top: 25px;
}
</style>
""", unsafe_allow_html=True)


@st.fragment(run_every="1s")
def clock():

    now = datetime.now(TIMEZONE)

    time_text = now.strftime("%I:%M:%S")
    ampm = now.strftime("%p")
    day = now.strftime("%A")
    date = now.strftime("%B %d, %Y")
    timezone = now.tzname()

    html = f"""
    <div class="clock-container">

        <div class="location">
            📍 Princeton Junction, New Jersey
        </div>

        <div class="time">
            {time_text}
        </div>

        <div class="ampm">
            {ampm}
        </div>

        <div class="day">
            {day}
        </div>

        <div class="date">
            {date}
        </div>

        <div class="timezone">
            Eastern Time — {timezone}
        </div>

    </div>
    """

    st.markdown(html, unsafe_allow_html=True)


clock()
