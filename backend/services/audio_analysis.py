import librosa

def analyze_audio(file_path: str, text: str) -> dict:
    """
    Analyze audio to get duration and WPM
    """
    try:
        y, sr = librosa.load(file_path)

        # Duration in seconds
        duration = librosa.get_duration(y=y, sr=sr)

        # Word count
        words = text.split()
        word_count = len(words)

        # Words per minute
        wpm = (word_count / duration) * 60 if duration > 0 else 0

        return {
            "duration_seconds": round(duration, 2),
            "word_count": word_count,
            "words_per_minute": round(wpm, 2)
        }

    except Exception as e:
        raise Exception(f"Audio Analysis Error: {str(e)}")