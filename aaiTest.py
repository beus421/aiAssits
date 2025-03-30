# `pip3 install assemblyai` (macOS)
# `pip install assemblyai` (Windows)
# testing assemblyai
import assemblyai as aai

aai.settings.api_key = "your api key"
transcriber = aai.Transcriber()

transcript = transcriber.transcribe("succulentChineseMeal.wav")

print(transcript.text)
