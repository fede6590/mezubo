import streamlit as st
import requests

# Streamlit app to interact with the Flask API
st.title('Roulette API')

# Make a request to the Flask API endpoint
response = requests.get('http://flask-api:5000/TEST')
data = response.json()

# Display the data in Streamlit
st.write('From API:')
st.json(data)
