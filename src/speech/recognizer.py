import requests
API_URL="https://api.sarvam.ai/speech-to-text"
LANGUAGES_CODES={
  "Telugu":"te-IN",
  "Hindi":"hi-IN",
  "English":"en-IN"
}
def transcribe_audio(audio_bytes,api_key,language):
  if not audio_bytes:
    raise ValueError("No audio received.")
  if not api_key:
    raise ValueError("Sarvam API Key is missing.")
  headers={
    "api-subscription-key":api_key
  }
  data={
    "model":"saaras:v4",
    "mode":"verbatim"
  }
  if language!="Automatic Detection":
    data["language_code"]=LANGUAGE_CODES[language]
    files={
      "file":(
        "recording.wav",audio_bytes,"audio/wav"
      )
    }
    response=requests.post(
      API_URL,headers=headers,
      data=data,
      files=files,
      timeout=90
    )
    if response.status_code!=200:
      raise RuntimeError(
        f"Speech recognition failed:{response.text}")
    result = response.json()
    return result["transcript"]
