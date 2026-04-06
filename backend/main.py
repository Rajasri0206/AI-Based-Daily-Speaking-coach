from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os

# Import services
from services.speech_to_text import transcribe_audio
from services.nlp_service import correct_grammar
from services.audio_analysis import analyze_audio
from services.scoring import calculate_score 
#new ------
from database.db import init_db, save_session

init_db()
#----------------
app = FastAPI(title="AI Speaking Coach API")

# Enable CORS (important for React frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Temporary folder for audio files
UPLOAD_FOLDER = "temp_audio"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# 🏠 Health Check
@app.get("/")
def home():
    return {"message": "AI Speaking Coach Backend Running 🚀"}


# 🎙️ Main API
@app.post("/analyze/")
async def analyze_audio_api(file: UploadFile = File(...)):
    try:
        # Validate file type
        if not file.filename.endswith((".wav", ".mp3", ".m4a")):
            raise HTTPException(status_code=400, detail="Unsupported file format")

        # Save file temporarily
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # 🔤 Step 1: Speech to Text
        transcript = transcribe_audio(file_path)

        # ✍️ Step 2: Grammar Correction
        corrected_text = correct_grammar(transcript)

        # 📊 Step 3: Audio Analysis
        audio_metrics = analyze_audio(file_path, transcript)

        # 🧮 Step 4: Simple Grammar Accuracy
        grammar_accuracy = (
            100 if transcript.strip() == corrected_text.strip() else 75
        )

        # 🎯 Step 5: Scoring
        scores = calculate_score(
            audio_metrics["words_per_minute"],
            grammar_accuracy
        )

        # 🧹 Clean up file
        os.remove(file_path)

        # ✅ Final Response
        return {
            "transcript": transcript,
            "corrected_text": corrected_text,
            "audio_metrics": audio_metrics,
            "scores": scores
        }
    #new----------------
        save_session(transcript, scores["overall_score"])

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))