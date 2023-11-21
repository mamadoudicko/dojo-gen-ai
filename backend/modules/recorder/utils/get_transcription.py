import os
import tempfile

import openai

openai.api_key = os.environ["OPENAI_API_KEY"]


def get_transcription(audio: bytes) -> str:
    """
    Return the transcription of the given audio data.
    """
    # Create a temporary WAV file with a name and get the transcription from openai
    transcription_model_name = "whisper-1"

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_file:
        temp_file.write(audio)
        temp_file.seek(0)
        transcript = openai.Audio.transcribe(transcription_model_name, file=temp_file)

    # Clean up the temporary file
    os.unlink(temp_file.name)
    return transcript["text"]
