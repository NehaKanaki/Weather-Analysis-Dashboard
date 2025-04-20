# 🌩 Weather Dashboard

An interactive, modern weather dashboard built with **Streamlit**, **Plotly**, and the **OpenWeatherMap API**. The app lets you enter any city and view real-time weather information along with visual charts for temperature, humidity, and weather distribution — all wrapped in a sleek dark-themed UI.

---

## 📸 Demo

![Weather Dashboard Screenshot](demo-screenshot.png) <!-- Add your screenshot path -->

---

## 🚀 Features

- 🔍 **Search Weather by City**
- 🌡 Real-time **Temperature, Humidity, Wind Speed**
- 📈 **Interactive Visualizations** using Plotly:
  - Bar chart (Temp & Humidity)
  - Line chart (Hourly Temp Trend - Mock)
  - Pie chart (Weather Condition Distribution - Mock)
- 🎨 **Dark Themed UI** with custom CSS styling
- 💡 Built using **Streamlit** for rapid deployment

---

## 🧰 Tech Stack

- [Streamlit](https://streamlit.io/)
- [Plotly](https://plotly.com/)
- [OpenWeatherMap API](https://openweathermap.org/api)
- [Python-dotenv](https://pypi.org/project/python-dotenv/)
- [Pandas](https://pandas.pydata.org/)

---

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/weather-dashboard.git
cd weather-dashboard 
```

### 2. Install dependencies
```
pip install -r requirements.txt
```
### 3.Set your API key securely using .env
Create a .env file in the root directory:
```
 API_KEY=your_openweathermap_api_key
```
### 4. Run the app
```
streamlit run app.py
```

