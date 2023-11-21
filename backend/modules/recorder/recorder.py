import streamlit as st

from backend.modules.recorder.utils.generate_chunks import generate_chunks
from backend.modules.recorder.utils.get_recorded_audio import get_recorded_audio
from backend.modules.recorder.utils.get_transcription import get_transcription
from backend.modules.recorder.utils.save_embeddings import save_embeddings


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
        transcription = get_transcription(audio_data)
        chunks = generate_chunks(transcription)
        save_embeddings(chunks)

        # Display audio data as received on the Python side
        col_playback, col_space = st.columns([0.58, 0.42])
        with col_playback:
            st.write(f"transcription: {transcription}")
            st.write(f"chunks: {chunks}")
            st.audio(audio_data, format="audio/wav")
