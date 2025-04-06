import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO

# API key and base URL
API_KEY = 'afb40866f9msh1b38ed3a5ecad6dp166027jsnfd784be96b17'
BASE_URL = 'https://23andme-23andme.p.rapidapi.com/'

# Function to fetch data from 23andMe API
def get_profile_data(profile_id):
    url = f"{BASE_URL}profile/{profile_id}/"
    headers = {
        'X-RapidAPI-Key': API_KEY,
        'X-RapidAPI-Host': '23andme-23andme.p.rapidapi.com'
    }
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()  # Returning the JSON response if successful
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

# Function to display profile picture
def show_profile_picture(profile_data):
    if 'profile_picture' in profile_data:
        st.image(profile_data['profile_picture'], caption='Profile Picture')
    else:
        st.warning("Profile picture not available.")

# Function to display ancestry
def show_ancestry(profile_data):
    if 'ancestry' in profile_data:
        ancestry = profile_data['ancestry']
        st.write("Ancestry Composition:")
        for region, percentage in ancestry.items():
            st.write(f"{region}: {percentage}%")
    else:
        st.warning("Ancestry data not available.")

# Function to display health-related data
def show_health_data(profile_data):
    if 'health' in profile_data:
        health_data = profile_data['health']
        st.write("Health Risk Information:")
        for condition, risk in health_data.items():
            st.write(f"{condition}: {risk}")
    else:
        st.warning("Health data not available.")

# Streamlit app layout
st.title("23andMe DNA Analysis")
st.sidebar.header("User Input")

# Profile ID input in the sidebar
profile_id = st.sidebar.text_input("Enter your Profile ID", "")

# If Profile ID is entered, fetch and display data
if profile_id:
    st.write(f"Fetching data for Profile ID: {profile_id}...")
    profile_data = get_profile_data(profile_id)
    
    if profile_data:
        # Show profile picture
        show_profile_picture(profile_data)
        
        # Show ancestry data
        show_ancestry(profile_data)
        
        # Show health-related data
        show_health_data(profile_data)

else:
    st.info("Please enter a Profile ID to fetch the data.")
