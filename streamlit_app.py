import streamlit as st
import requests

# Set the app title 
st.title('FIKRI STREAMLIT')

# Add a welcome message 
st.write('Welcome to Fikri Streamlit app!')

# Create a text input 
widgetuser_input = st.text_input('Enter a custom message:', 'Hello, Fikri Streamlit!')
st.write('Customized Message:', widgetuser_input)

# Weather Forecast Section
st.header("Weather Forecast")

# Input for location
location = st.text_input("Enter a location for weather forecast:", "Jakarta")

# API key for OpenWeatherMap (replace with your real API key)
api_key = "YOUR_API_KEY"  # <- Replace this with your actual API key

# Make API request
if location:
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(weather_url)

    if response.status_code == 200:
        data = response.json()
        st.subheader(f"Weather in {location}")
        st.write(f"**Temperature:** {data['main']['temp']}°C")
        st.write(f"**Condition:** {data['weather'][0]['description'].title()}")
        st.write(f"**Humidity:** {data['main']['humidity']}%")
        st.write(f"**Wind Speed:** {data['wind']['speed']} m/s")
    else:
        st.error(f"Could not fetch weather data for '{location}'. Please check the city name.")




