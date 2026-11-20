import streamlit as st
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
  "Tap here to record",sample_rate=16000
)
#display recorder audio
if audio_file is not None:
  st.audio(audioi_file,format="audio/wav")
  st.success("Voice recording captured successfully!")
  st.write("Selected language:",language)
  st.info("Speech recognition engine will be connected in the next step.")
else:
  st.write("Record your voice to get started.")



  
