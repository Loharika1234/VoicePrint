import streamlit as st
from src.speech.audio_processor import load_audio
#configure the application
st.set_page_config(
  page_title="VoicePrint",
  page_icon="🎤",
  layout="centered"
)
#application heading
st.title("🎤Voice Print")
st.caption("Multilingual Speech-to-text Converter")
st.divider()
#language selection
language=st.selectbox(
  "Select your language",
  ["Automatic Detection","Telugu","Hindi","English"]
)
#voice recording
st.subheader("Record your Voice")
audio_file=st.audio_input(
  "Tap here to record",
  sample_rate=16000
)
#display recorder audio
if audio_file is not None:
  st.audio(audio_file,format="audio/wav")
  try:
    audio_bytes=audio_file.getvalue()
    audio_data,sample_rate=load_audio(audio_bytes)
    duration =len(audio_data)/sample_rate
    st.success("Audio processed Successfully")
    st.write("Selected language:",language)
    st.write("Sample Rate:",f"{sample_rate}Hz")
    st.write("Audio duration:",f"{duration:.2f}seconds")
    st.write("Audio Samples:",len(audio_data))
  except ValueError as error:
    st.error(str(error))
else:
  st.info("Record your voice to get started.")



  
