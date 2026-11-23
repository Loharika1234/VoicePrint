import streamlit as st
from src.speech.audio_processor import load_audio
from src.speech.recognizer import transcribe_audio
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
if "transcript" not in st.session_state:
  st.session_state.transcript=""
if audio_file is not None:
  st.audio(audio_file,format="audio/wav")
  try:
    audio_bytes=audio_file.getvalue()
    audio_data,sample_rate=load_audio(audio_bytes)
    duration =len(audio_data)/sample_rate
    st.success("Audio processed Successfully")
    
    st.write("Audio duration:",f"{duration:.2f}seconds")
    if duration>30:
      st.error("Recording exceeds 30 seconds.Please record a shorter clip.")
    elif st.button("🎤 transcibe audio"):
      api_key=st.secrets.get("sk_3colcoa0_J9oQbVj4DYyURpr2pbGFC57S")
      st.write("API key loaded:",bool(api_key))
      if not api_key:
        st.error("Sarvam API key is missing.")
      else:
        with st.spinner("Transcribing your audio..."):
              transcript=transcribe_audio(
                audio_bytes,api_key,language
              )
              st.sessiom_state.transcript=transcript
              st.success("Transcription completed!")
  except Exception as error:
        st.error(f"Error:{error}")
  if st.session_state.transcript:
      st.subheader("Your Transcript")
      st.text_area("Edit your transcript if needed.",key="transcript",height=180)
else:
  st.info("Record your voice to get started.")



  
