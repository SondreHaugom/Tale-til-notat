import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

audio_file = "audioFile/opptak-1777285349556.mp3"

client = OpenAI(
    api_key= os.getenv("OPENAI_API_KEY")
)




def transcribe_audio(file_path):
    file_path = audio_file
    if not os.path.isfile(file_path):
        print(f"Filen '{file_path}' finnes ikke.")
        return None
    try:
        transcription = client.audio.transcriptions.create(
            model="gpt-4o-mini-transcribe",
            file=open(file_path, "rb"),
        )
        return transcription.text
    except Exception as e:
        print(f"En feil oppsto under transkripsjon: {e}")
        return None
    
if __name__ == "__main__":
    transcription_result = transcribe_audio(audio_file)
    if transcription_result:
        print("Transkripsjon:", transcription_result)

