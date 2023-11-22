import streamlit as st

from backend.modules.recorder.utils.embed_and_save_chunks import embed_and_save_chunks
from backend.modules.recorder.utils.generate_chunks import generate_chunks
from backend.modules.recorder.utils.get_answer import get_answer
from backend.modules.recorder.utils.get_recorded_audio import get_recorded_audio
from backend.modules.recorder.utils.get_transcription import get_transcription


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
        transcription = get_transcription(audio_data)
        st.write("Transcription:", transcription)

        transcription_chunks = generate_chunks(transcription)

        embed_and_save_chunks(transcription_chunks)

        question = st.text_input(
            label="Question", placeholder="Enter a question please"
        )

        if question:
            answers = []
            for transcription_chunk in transcription_chunks:
                message = f"""
                Context: {transcription_chunk}
                Question: {question}
                If the answer is not in the context above, please answer with empty string "".
                Answer:
                """

                answers.append(get_answer(message))

            # Join the answers into a single string
            answer = " ".join(answers)

            st.write("Answer:", answer)
