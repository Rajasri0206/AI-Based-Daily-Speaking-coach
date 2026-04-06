import whisper

# Load model once (important for performance)
model = whisper.load_model("base")

def transcribe_audio(file_path: str) -> str:
    """
    Converts audio file to text using Whisper
    """
    try:
        result = model.transcribe(file_path)
        return result.get("text", "").strip()
    except Exception as e:
        raise Exception(f"Speech-to-Text Error: {str(e)}")