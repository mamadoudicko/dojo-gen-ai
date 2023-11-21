import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from backend.modules.recorder.recorder import recorder

# Set Streamlit page configuration
st.set_page_config(page_title="Audio Recorder and Chat")

# Create a state variable to control page navigation
page = st.sidebar.radio("Select a page", ["Audio Recorder"])

recorder()
