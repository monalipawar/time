import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Current Time",
    page_icon="🕐",
    layout="centered"
)

components.html(
    """
    <html>
    <head>
        <style>
            body {
                margin: 0;
                background: linear-gradient(135deg, #0f172a, #1e293b);
                font-family: Arial, sans-serif;
            }

            .clock-container {
                background: #111827;
                border-radius: 30px;
                padding: 40px 20px;
                text-align: center;
                margin: 20px auto;
                max-width: 650px;
                box-shadow: 0 15px 50px rgba(0,0,0,0.45);
            }

            .location {
                font-size: 22px;
                color: #cbd5e1;
                margin-bottom: 25px;
            }

            .time {
                font-family: monospace;
                font-size: 70px;
                font-weight: bold;
                color: white;
                letter-spacing: 4px;
            }

            .ampm {
                font-size: 24px;
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
    </head>

    <body>

        <div class="clock-container">

            <div class="location">
                📍 Princeton Junction, New Jersey
            </div>

            <div class="time" id="time">
                00:00:00
            </div>

            <div class="ampm" id="ampm">
                AM
            </div>

            <div class="day" id="day">
                Wednesday
            </div>

            <div class="date" id="date">
                August 19, 2026
            </div>

            <div class="timezone" id="timezone">
                Eastern Time
            </div>

        </div>

        <script>
            function updateClock() {

                const now = new Date();

                const options = {
                    timeZone: "America/New_York",
                    hour: "2-digit",
                    minute: "2-digit",
                    second: "2-digit",
                    hour12: true
                };

                const timeParts = new Intl.DateTimeFormat(
                    "en-US",
                    options
                ).formatToParts(now);

                let hour = "";
                let minute = "";
                let second = "";
                let dayPeriod = "";

                timeParts.forEach(part => {
                    if (part.type === "hour") hour = part.value;
                    if (part.type === "minute") minute = part.value;
                    if (part.type === "second") second = part.value;
                    if (part.type === "dayPeriod") dayPeriod = part.value;
                });

                document.getElementById("time").textContent =
                    `${hour}:${minute}:${second}`;

                document.getElementById("ampm").textContent =
                    dayPeriod;


                const dateOptions = {
                    timeZone: "America/New_York",
                    weekday: "long",
                    month: "long",
                    day: "numeric",
                    year: "numeric"
                };

                document.getElementById("date").textContent =
                    new Intl.DateTimeFormat(
                        "en-US",
                        dateOptions
                    ).format(now);


                const dayOptions = {
                    timeZone: "America/New_York",
                    weekday: "long"
                };

                document.getElementById("day").textContent =
                    new Intl.DateTimeFormat(
                        "en-US",
                        dayOptions
                    ).format(now);


                const timezoneOptions = {
                    timeZone: "America/New_York",
                    timeZoneName: "short"
                };

                const timezoneParts =
                    new Intl.DateTimeFormat(
                        "en-US",
                        timezoneOptions
                    ).formatToParts(now);

                const timezoneName =
                    timezoneParts.find(
                        part => part.type === "timeZoneName"
                    );

                document.getElementById("timezone").textContent =
                    "Eastern Time — " +
                    (timezoneName ? timezoneName.value : "ET");
            }

            updateClock();

            setInterval(updateClock, 1000);
        </script>

    </body>
    </html>
    """,
    height=500,
)
