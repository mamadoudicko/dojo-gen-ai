import streamlit as st
from streamlit_audiorec import st_audiorec

st.title("Audio Recorder Example")

# Create an instance of the audio recorder
recorder = st_audiorec()

# Display the recorder widget
if st.button("Start Recording"):
    recorder.start()

if st.button("Stop Recording"):
    recorder.stop()

# Display the recorded audio
if recorder.audio_data:
    st.audio(recorder.audio_data, format="audio/wav")

# Clear the recorded audio
if st.button("Clear Recording"):
    recorder.clear()
