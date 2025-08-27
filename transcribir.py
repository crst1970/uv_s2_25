import whisper

# Cargar modelo (elige según tu PC: tiny, base, small, medium, large)
model = whisper.load_model("small")

# Archivo de entrada
audio_file = "Colo1.mp3"

# Transcribir
result = model.transcribe(audio_file, language="es")

# Texto completo
texto = result["text"]

# Dividir en párrafos cada vez que aparece un punto seguido
parrafos = texto.split(". ")

# Guardar en archivo TXT
with open("Colo1_transcripcion.txt", "w", encoding="utf-8") as f:
    for p in parrafos:
        f.write(p.strip() + "\n\n")

print("✅ Transcripción guardada en Colo1_transcripcion.txt")
