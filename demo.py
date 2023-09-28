import streamlit as st

from st_audiorec import st_audiorec

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
        # Display audio data as received on the Python side
        col_playback, col_space = st.columns([0.58, 0.42])
        with col_playback:
            st.audio(wav_audio_data, format='audio/wav')

def chat_page():
    """
    Render the Chat Page.
    """
    st.title("Chat Page")
    st.write("This is the Chat Page. You can chat with content here.")
    # Add a chat input box, and you can process and display chat messages here.

# Conditionally render pages based on the selected page
if page == "Audio Recorder":
    audiorec_demo_app()
elif page == "Chat Page":
    chat_page()
