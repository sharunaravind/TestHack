# audio_utils/recorder.py

import streamlit as st
import tempfile

def upload_audio():
    """
    Lets user upload a .wav or .mp3 file. Stores it temporarily and returns its path.
    """
    audio_file = st.file_uploader("🎙️ Upload your inspection audio", type=["wav", "mp3", "m4a"])

    if audio_file is not None:
        # Save to a temp file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            tmp.write(audio_file.read())
            return tmp.name
    
    return None
