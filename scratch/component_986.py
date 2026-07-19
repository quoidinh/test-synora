# transcribe_cpu.py
from faster_whisper import WhisperModel
import sys

audio_path = "/workspace/17674900446098234623519984162735152.mp3"

# CPU mode, int8 quantization để nhẹ và nhanh
model = WhisperModel("base", device="cpu", compute_type="int8")

segments, info = model.transcribe(audio_path, beam_size=5)

print(f"Language detected: {info.language}")
print("--- Transcript ---")
with open("/workspace/transcript.txt", "w", encoding="utf-8") as f:
    for seg in segments:
        line = f"[{seg.start:.1f}s -> {seg.end:.1f}s] {seg.text}"
        print(line)
        f.write(line + "\\n")

print("\nSaved to /workspace/transcript.txt")
