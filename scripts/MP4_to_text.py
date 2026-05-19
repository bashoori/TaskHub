import whisper
from pathlib import Path

# ==============================
# PATHS
# ==============================

video_path = "input/AI_effect.mp4"
output_file = "output/AI_effect.txt"

# ==============================
# SETTINGS
# ==============================

language = "en"       # fa = Persian | en = English
model_size = "base"   # tiny, base, small, medium, large

# ==============================
# CHECK FILE
# ==============================

if not Path(video_path).exists():
    raise FileNotFoundError(f"❌ File not found: {video_path}")

# Create output folder if missing
Path("output").mkdir(exist_ok=True)

# ==============================
# LOAD MODEL
# ==============================

print(f"Loading Whisper model: {model_size}")

model = whisper.load_model(model_size)

# ==============================
# TRANSCRIBE
# ==============================

print("Transcribing video... please wait.")

result = model.transcribe(
    video_path,
    language=language,
    fp16=False
)

# ==============================
# SAVE TXT
# ==============================

with open(output_file, "w", encoding="utf-8") as f:
    f.write(result["text"])

# ==============================
# DONE
# ==============================

print("\n✅ Transcription complete!")
print(f"📄 Saved as: {output_file}")