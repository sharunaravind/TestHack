# transcriber/whisper_engine.py

import whisper
import os

# Load and cache model only once
_loaded_models = {}

def transcribe_audio(audio_path: str, model_size: str = "base") -> str:
    """
    Transcribes speech from the given audio file using Whisper.

    Args:
        audio_path (str): Path to the audio file (.wav, .mp3, etc.)
        model_size (str): Model size to use ("tiny", "base")

    Returns:
        str: Transcribed text
    """
    if not os.path.isfile(audio_path):
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    # Lazy load + reuse models to avoid loading repeatedly
    if model_size not in _loaded_models:
        print(f"⏳ Loading Whisper model: {model_size} ...")
        _loaded_models[model_size] = whisper.load_model(model_size)
        print(f"✅ Model loaded.")

    model = _loaded_models[model_size]

    print(f"🎙️ Transcribing: {audio_path} ...")
    result = model.transcribe(audio_path)
    return result["text"].strip()
