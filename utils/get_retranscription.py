import os
import tempfile

import openai

openai.api_key = os.environ["OPENAI_API_KEY"]


def get_retranscription(audio: bytes):
    """
    Return the retrotranscription of the given audio data.
    """
    # Create a temporary WAV file with a name
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_file:
        temp_file.write(audio)
        temp_file.seek(0)
        transcript = openai.Audio.transcribe("whisper-1", file=temp_file)

    # Clean up the temporary file
    os.unlink(temp_file.name)
    return transcript['text']
