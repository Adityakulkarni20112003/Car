"""This module creates the home page."""

# Import necessary modules.
import streamlit as st

def app():
    st.title("Car Pridiction app")
   
    st.text(
        """
        This web app allows a user to predict the prices of a car based on their 
        engine size, horse power, dimensions and the drive wheel type parameters.
        """
    )