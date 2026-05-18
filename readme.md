# Tale til notat

Dette prosjektet lar deg transkribere lydopptak til tekst ved hjelp av ulike AI-tjenester (Mistral, OpenAI, ElevenLabs).

## Funksjoner
- Transkriber lydfiler (f.eks. MP3) til tekst
- Støtte for flere leverandører: Mistral, OpenAI, ElevenLabs
- Enkel å utvide med flere API-nøkler og lydfiler

## Kom i gang
1. Legg inn dine API-nøkler i en `.env`-fil:
   - `MISTRALAI_API_KEY`
   - `OPENAI_API_KEY`
   - `ELEVENLABS_API_KEY`
2. Plasser lydfilene i `audioFile/`-mappen.
3. Kjør ønsket transkripsjonsskript, f.eks.:
   ```bash
   python mistrat-transcription.py
   ```

## Avhengigheter
- Python 3.10+
- Se `requirements.txt` eller installer med `uv pip install -r requirements.txt`

## Filstruktur
- `audioFile/` – Lydfiler for transkripsjon
- `mistrat-transcription.py` – Bruker Mistral
- `GPT-4o-transcribe.py` – Bruker OpenAI
- `evenLabs.py` – Bruker ElevenLabs
- `whisper.py` – (Egen Whisper-implementasjon)

## Lisens
MIT
