import streamlit as st

from backend.modules.recorder.utils.get_recorded_audio import get_recorded_audio


def recorder():
    """
    Render the Audio Recorder page.
    """
    st.title("Audio Recorder")
    st.write("\n\n")

    audio_data = get_recorded_audio()  # That's it! :D

    # Add some spacing and informative messages
    col_info, col_space = st.columns([0.57, 0.43])

    with col_info:
        st.write("\n" * 2)  # Add vertical spacer

    if audio_data is not None:
        # write audio data
        print("audio_data is", audio_data)
