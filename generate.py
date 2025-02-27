import requests
import json
from pydub import AudioSegment

API_KEY = "sk_ed5ae53449821f8cd20579cb419c489da27ae3d1aadbc99e"
VOICE_ID = "Oq0cIHWGcnbOGozOQv0t"  # Select an appropriate Indian voice


def generate_tts(text, output_file="output.wav"):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": API_KEYgit push -u origin main

    }

    data = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        temp_mp3 = "temp_output.mp3"
        with open(temp_mp3, "wb") as f:
            f.write(response.content)

        # Convert MP3 to WAV
        audio = AudioSegment.from_mp3(temp_mp3)
        audio.export(output_file, format="wav")

        print(f"Audio saved to {output_file}")
    else:
        print(f"Error: {response.text}")


# Use the script from the assignment
script = """Namaste Mathangi! My name is Anika, and I'm here to guide you through managing your credit
card dues. Mathangi, as of today, your credit card bill shows an amount due of INR 5,053 which
needs to be paid by 31st December 2024
Missing this payment could lead to two significant consequences:
First, a late fee will be added to your outstanding balance.
Second, your credit score will be negatively impacted, which may affect your future borrowing
ability.
Make your payment by clicking the link here... Pay through UPI or bank transfer. Thank you!"""

generate_tts(script, "Wav2Lip/gulab.wav")
