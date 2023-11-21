import os
from io import BytesIO

import numpy as np
import streamlit as st
import streamlit.components.v1 as components


def get_recorded_audio():
    """
    Display the Audio Recorder component and return the recorded audio data.
    """
    # get our custom component path relative to current directory
    parent_dir = os.path.dirname(__file__)
    build_dir = os.path.join(parent_dir, "../../../../frontend/build")

    # get our custom component
    audio_recorder = components.declare_component("audio_recorder", path=build_dir)

    # Create an instance of the component: STREAMLIT AUDIO RECORDER
    audio_data_as_buffer = audio_recorder()

    # Since the returned data is in the form of arraybuffer, we need to convert it to bytes
    audio_data_as_bytes = None
    if isinstance(audio_data_as_buffer, dict):
        with st.spinner("Retrieving audio-recording..."):
            ind, audio_data_as_buffer = zip(*audio_data_as_buffer["arr"].items())
            ind = np.array(ind, dtype=int)  # convert to np array
            audio_data_as_buffer = np.array(audio_data_as_buffer)  # convert to np array
            sorted_ints = audio_data_as_buffer[ind]
            stream = BytesIO(b"".join([int(v).to_bytes(1, "big") for v in sorted_ints]))
            audio_data_as_bytes = stream.read()

    return audio_data_as_bytes
