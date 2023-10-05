import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from st_audiorec import st_audiorec
from utils.generate_chunks import generate_chunks
from utils.get_answer import get_answer
from utils.get_retranscription import get_retranscription
from utils.save_embeddings import save_embeddings

# Set Streamlit page configuration
st.set_page_config(page_title="Audio Recorder and Chat")

# Create a state variable to control page navigation
page = st.sidebar.radio("Select a page", ["Audio Recorder", "Chat Page"])

def audiorec_demo_app():
    """
    Render the Audio Recorder page.
    """
    # TITLE and Creator information
    st.title('Audio Recorder')
    st.write('\n\n')

    # TUTORIAL: How to use STREAMLIT AUDIO RECORDER?
    # By calling this function, an instance of the audio recorder is created.
    # Once a recording is completed, audio data will be saved to wav_audio_data.
    wav_audio_data = st_audiorec()  # That's it! :D

    # Add some spacing and informative messages
    col_info, col_space = st.columns([0.57, 0.43])
    with col_info:
        st.write('\n' * 2)  # Add vertical spacer
        st.write('The .wav audio data, as received in the backend Python code,'
                 ' will be displayed below this message as soon as it has'
                 ' been processed. [This informative message is not part of'
                 ' the audio recorder and can be removed easily] 🎈')

    if wav_audio_data is not None:
        retranscription = get_retranscription(wav_audio_data)
        chunks = generate_chunks(retranscription)
        save_embeddings(chunks)

        # Display audio data as received on the Python side
        col_playback, col_space = st.columns([0.58, 0.42])
        with col_playback:
            st.write(f"retranscription: {retranscription}")
            st.write(f"chunks: {chunks}")
            st.audio(wav_audio_data, format='audio/wav')


def chat_page():
    """
    Render the Chat Page.
    """
    st.title("Chat Page")
    st.write("This is the Chat Page. You can chat with content here.")

    # Add a text input for users to enter their questions
    user_question = st.text_input("Enter your question:")
    
    if st.button("Submit"):
        if user_question:
            # Process the user's question and get the answer
            answer = get_answer(user_question)
            st.write(f"Question: {user_question}")
            st.write(f"Answer: {answer}")

# Conditionally render pages based on the selected page
if page == "Audio Recorder":
    audiorec_demo_app()
elif page == "Chat Page":
    chat_page()
