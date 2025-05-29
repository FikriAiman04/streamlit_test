import streamlit as st
import requests

# Set the app title 
st.title('FIKRI STREAMLIT')

# Add a welcome message 
st.write('Welcome to Fikri Streamlit app!')

# Create a text input 
widgetuser_input = st.text_input('Enter a custom message:', 'Hello, Fikri Streamlit!')

# Display the customized message 
st.write('Customized Message:', widgetuser_input)

# Dropdown to select base currency
currencies = ['USD', 'EUR', 'GBP', 'JPY', 'AUD', 'CAD', 'CHF', 'CNY', 'SEK', 'NZD']  # Add more as needed
base_currency = st.selectbox('Select Base Currency:', currencies)

# API call using the selected base currency
response = requests.get(f'https://api.vatcomply.com/rates?base={base_currency}')

# Display the results
if response.status_code == 200:
    data = response.json()
    st.write(f'Exchange rates for base currency: {base_currency}')
    st.json(data)
else:
    st.error(f"API call failed with status code: {response.status_code}")



