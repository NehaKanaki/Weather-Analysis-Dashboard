# Import necessary libraries
import streamlit as st  # Streamlit for building the web interface
import requests  # To send HTTP requests to fetch weather data
import pandas as pd  # For working with tabular data
import random  # To generate mock/random data for visualizations
import plotly.express as px  # For interactive plots and charts
import os
from dotenv import load_dotenv

load_dotenv()  

# Set up the Streamlit page configuration: title and layout
st.set_page_config(page_title="🌩 Weather Dashboard", layout="wide")

# Inject custom CSS to apply dark theme styling to the app # markdown- Used to add html and css to the streamlit app
st.markdown("""                              
    <style>
    body {
        background-color: #0E1117;  /* Dark background for body */
        color: #FAFAFA;  /* Light text for readability */
    }
    .main {
        background-color: #0E1117;  /* Main area background */
    }
    .block-container {
        padding-top: 2rem;  /* Padding on top */
    }0
    .title {
        font-size: 3rem;
        font-weight: 800;
        color: #00FFE3;  /* Accent color */
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-box {
        background-color: #1E1E2F;  /* Card background */
        border: 1px solid #292929;
        padding: 30px;
        border-radius: 18px;
        text-align: center;
        box-shadow: 0 0 12px rgba(0, 255, 227, 0.1);
        margin-bottom: 20px;
        color: white;
    }
    .metric-box h3 {
        color: #BBBBBB;
        font-weight: 500;
        margin-bottom: 10px;
    }
    .metric-value {
        font-size: 2.5rem;
        font-weight: 700;
        color: #00FFE3;
    }
    </style>
""", unsafe_allow_html=True)

# More custom styling for a modified dark theme
st.markdown("""
    <style>
    body {
        background-color: #0D0F1C;
        color: #E0E6ED;
    }
    .main {
        background-color: #0D0F1C;
    }
    .block-container {
        padding-top: 2rem;
    }
    .title {
        font-size: 3rem;
        font-weight: 800;
        color: #00C9A7;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-box {
        background-color: #1A1C2B;
        border: 1px solid #33364D;
        padding: 30px;
        border-radius: 18px;
        text-align: center;
        box-shadow: 0 0 20px rgba(31, 255, 198, 0.08);
        margin-bottom: 20px;
        color: #E0E6ED;
    }
    .metric-box h3 {
        color: #B0B8C4;
        font-weight: 500;
        margin-bottom: 10px;
    }
    .metric-value {
        font-size: 2.7rem;
        font-weight: 700;
        color: #1FFFC6;
    }
    </style>
""", unsafe_allow_html=True)

# api_key = os.getenv("API_KEY")
api_key = st.secrets["api_key"]

# Sidebar input: allows user to enter a city name
st.sidebar.markdown("## 📍 Location")
city = st.sidebar.text_input("Enter City Name", "Pune")  # Default city is Pune

# Construct the URL for OpenWeatherMap API with units in metric
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# Send request to the weather API
response = requests.get(url)

# If the response is successful (status code 200), process and display data
if response.status_code == 200:
    data = response.json()  # Parse the JSON response
    temp = data["main"]["temp"]  # Current temperature
    feels_like = data["main"]["feels_like"]  # "Feels like" temperature
    humidity = data["main"]["humidity"]  # Humidity percentage
    wind_speed = data["wind"]["speed"]  # Wind speed in m/s
    condition = data["weather"][0]["description"].title()  # Weather condition text

    # Create three metric cards for temperature, humidity, and wind speed
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"<div class='metric-box'><h3>🌡 Temperature</h3><div class='metric-value'>{temp} °C</div></div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='metric-box'><h3>💧 Humidity</h3><div class='metric-value'>{humidity} %</div></div>", unsafe_allow_html=True)
    with col3:
        st.markdown(f"<div class='metric-box'><h3>💨 Wind Speed</h3><div class='metric-value'>{wind_speed} m/s</div></div>", unsafe_allow_html=True)

    # Display detailed weather summary below the cards
    st.markdown("### 🔍 Detailed Summary")
    st.markdown(f"*Feels Like:* {feels_like} °C")  # Feels-like temperature
    st.markdown(f"*Condition:* {condition}")  # Weather description

    # ---------------- VISUAL CHARTS SECTION ----------------

    st.markdown("### 📊 Visual Analysis")

    # Bar chart showing temperature and humidity
    bar_data = pd.DataFrame({
        "Metric": ["Temperature (°C)", "Humidity (%)"],
        "Value": [temp, humidity]
    })
    bar_fig = px.bar(
        bar_data, x="Metric", y="Value", color="Metric",
        color_discrete_sequence=["#00FFE3", "#FF6EC7"],
        title="Temperature & Humidity"
    )
    st.plotly_chart(bar_fig, use_container_width=True)

    # Line chart for mock hourly temperature data (randomized)
    hourly_data = pd.DataFrame({
        "Hour": list(range(1, 13)),  # 12-hour trend
        "Temperature": [round(temp + random.uniform(-2, 2), 1) for _ in range(12)]
    })
    line_fig = px.line(
        hourly_data, x="Hour", y="Temperature",
        title="Hourly Temperature Trend",
        markers=True, line_shape='spline',
        color_discrete_sequence=["#00FFE3"]
    )
    st.plotly_chart(line_fig, use_container_width=True)

    # Pie chart showing mock distribution of different weather conditions
    pie_data = pd.DataFrame({
        "Condition": ["Clear", "Cloudy", "Rainy", "Windy"],
        "Percentage": [random.randint(10, 30) for _ in range(4)]
    })
    pie_fig = px.pie(
        pie_data, names='Condition', values='Percentage',
        title="Weather Type Distribution (Mock)",
        color_discrete_sequence=px.colors.sequential.Teal
    )
    st.plotly_chart(pie_fig, use_container_width=True)

else:
    # Display error if API response is not successful
    st.error("❌ Could not fetch weather data. Please check the city name.") 