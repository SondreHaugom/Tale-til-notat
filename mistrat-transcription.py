import os
from mistralai.client import Mistral
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("MISTRAL_API_KEY")
if not api_key:
    raise ValueError("MISTRAL_API_KEY environment variable is not set.")
model = "voxtral-mini-2602"

client = Mistral(api_key=api_key)


"""
with open("audioFile/opptak-1777285349556.mp3", "rb") as f:
    transcription_response = client.audio.transcriptions.complete(
        model=model,
        file={
            "content": f,
            "file_name": "audio.mp3",
        },
        ## language="en"
    )

print(transcription_response.text)

"""

def mistral_transcribe_audio():
    with open("audioFile/opptak-1777285349556.mp3", "rb") as f:
        transcription_response = client.audio.transcriptions.complete(
            model=model,
            file={
                "content": f,
                "file_name": "audio.mp3",
            },
        )
        if transcription_response.text:
            return transcription_response.text
        else:
            raise ValueError("Transcription failed, no text returned.")
        
if __name__ == "__main__":
    try:
        transcription = mistral_transcribe_audio()
        print(transcription)
    except Exception as e:
        print(f"An error occurred during transcription: {e}")