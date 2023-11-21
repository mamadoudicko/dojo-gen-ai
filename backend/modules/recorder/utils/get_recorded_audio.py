import os
from io import BytesIO

import numpy as np
import streamlit as st
import streamlit.components.v1 as components


def get_recorded_audio():
    """
    Display the Audio Recorder component and return the recorded audio data.
    """
    # Get our custom component path relative to the current directory
    parent_dir = os.path.dirname(__file__)
    build_dir = os.path.join(parent_dir, "../../../../frontend/build")

    # Get our custom component
    audio_recorder = components.declare_component("audio_recorder", path=build_dir)

    # Create an instance of the component: STREAMLIT AUDIO RECORDER
    audio_data_as_buffer = audio_recorder()

    # Convert array buffer to bytes
    audio_data_as_bytes = None
    if isinstance(audio_data_as_buffer, dict) and "arr" in audio_data_as_buffer:
        with st.spinner("retrieving audio-recording..."):
            ind, raw_audio_data = zip(*audio_data_as_buffer["arr"].items())
            ind = np.array(ind, dtype=int)  # convert to np array
            raw_audio_data = np.array(raw_audio_data)  # convert to np array
            sorted_ints = raw_audio_data[ind]
            stream = BytesIO(b"".join([int(v).to_bytes(1, "big") for v in sorted_ints]))
            # wav_bytes contains audio data in byte format, ready to be processed further
            audio_data_as_bytes = stream.read()

    return audio_data_as_bytes
