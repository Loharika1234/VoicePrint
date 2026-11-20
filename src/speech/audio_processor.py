from io import BytesIO
import numpy as np
import soundfile as sf
def load_audio(audio_bytes):
  if not audio_bytes:
    raise ValueError("No audio data received.")
  try:
    audio_data,sample_rate=sf.read(
      BytesIO(audio_bytes),
      dtype="float32"
    )
  except Exception as error:
    raise ValueError("Unable to read audio file.") from error
  if audio_data.size==0:
    raise ValueError("Audio file is empty.")
  #convert stereo audio into mono
  if audio_data.ndim>1:
    audio_data=np.mean(audio_data,axis=1)
  return audio_data,sample_rate
