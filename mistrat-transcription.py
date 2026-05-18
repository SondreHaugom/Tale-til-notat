import os
from mistralai.client import Mistral
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("MISTRAL_API_KEY")
if not api_key:
    raise ValueError("MISTRAL_API_KEY environment variable is not set.")
model = "voxtral-mini-latest"

client = Mistral(api_key=api_key)

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