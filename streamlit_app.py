import streamlit as st
from gtts import gTTs
from io import BytesIO


st.title("Simple Text to Speech Converter")

text_input = st.text_area("Enter text to convert to speech")

language = st.selectbox("Select language",["en","fr","ru","hi","es"])

if st.button("Generate my speech"):
  if text_inmput:
    tts = gTTS(text_input, lang=language)

    audio_stream = BytesIO()

    tts.write_to_fp(audio_stream)

    st.audio(audio_stream)
  else:
    st.warning("Please enter some text.")
