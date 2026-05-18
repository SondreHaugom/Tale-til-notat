# example.py
import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

load_dotenv()

elevenlabs = ElevenLabs(
  api_key=os.getenv("ELEVENLABS_API_KEY"),
)

print("Nå skal commit funke!!!")

# Funksjon for å transkribere en lydfil ved hjelp av ElevenLabs API
def transcribe_audio_file(audio_file_path):
    script_dir = os.path.dirname(__file__)
    audio_file_path = os.path.join(script_dir, "audioFile", "opptak-1777285349556.mp3")
    print("audio_file_path:", audio_file_path)
    if not os.path.isfile(audio_file_path):
        print(f"File not found: {audio_file_path}")
        return None
    
    transcription = elevenlabs.speech_to_text.convert(
        file=open(audio_file_path, "rb"),
        model_id="scribe_v2", # Model to use
        tag_audio_events=True, # Tag audio events like laughter, applause, etc.
        language_code=None, # Auto-detect language
        diarize=True, # Whether to annotate who is speaking
    )

    if not transcription:
        return None
    return transcription

if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)
    audio_file_path = os.path.join(script_dir, "audioFile", "opptak-1777285349556.mp3")
    transcription = transcribe_audio_file(audio_file_path)

    if transcription:
        print("Transcription:")
        print(transcription.text)
    else:
        print("Failed to transcribe the audio file.")
