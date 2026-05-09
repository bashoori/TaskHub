import sys, argparse, os
from pathlib import Path

# Make bundled ffmpeg available to whisper
try:
    import imageio_ffmpeg
    ffmpeg_dir = os.path.dirname(imageio_ffmpeg.get_ffmpeg_exe())
    os.environ["PATH"] = ffmpeg_dir + os.pathsep + os.environ.get("PATH", "")
except ImportError:
    pass  # fall back to system ffmpeg if available

def convert(mp3_path, output_dir=None, model="base"):
    import whisper
    mp3_path = Path(mp3_path)
    if not mp3_path.exists():
        raise FileNotFoundError(f"File not found: {mp3_path}")
    out_dir = Path(output_dir) if output_dir else mp3_path.parent
    out_dir.mkdir(parents=True, exist_ok=True)
    output_path = out_dir / mp3_path.with_suffix(".txt").name
    print(f"\nTranscribing '{mp3_path.name}'...")
    result = m.transcribe(str(mp3_path))
    text = result["text"].strip()
    output_path.write_text(text, encoding="utf-8")
    print(f"Saved to '{output_path}'")
    print("\n--- Preview ---\n" + text[:500])

parser = argparse.ArgumentParser()
parser.add_argument("input", help="MP3 file or folder containing MP3 files")
parser.add_argument("-o", "--output", default=None, help="Output folder for .txt files")
parser.add_argument("--model", default="base")
args = parser.parse_args()

input_path = Path(args.input)
mp3_files = sorted(input_path.glob("*.mp3")) if input_path.is_dir() else [input_path]

if not mp3_files:
    print("No MP3 files found.")
    sys.exit(1)

import whisper
print(f"Loading Whisper model '{args.model}'...")
m = whisper.load_model(args.model)
print(f"Found {len(mp3_files)} file(s) to transcribe.")

for mp3 in mp3_files:
    convert(mp3, args.output, args.model)

print("\nAll done!")