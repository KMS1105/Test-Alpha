#import os
#from gtts import gTTS
#from playsound import playsound
#from pydub import AudioSegment
import streamlit as st
import openai
#import time
#import re

"""https://www.youtube.com/watch?v=8u2PngR2xpM, Terminal=streamlit run (File Path)"""

st.title("Test")

with st.form("form"):
    User_input = st.text_input("Prompt")
    size = st.selectbox("Size", ["1024x1024", "512x512", "256x256"])
    submit = st.form_submit_button("Submit")

if submit and User_input:
    GPT_Prompt = [{
        "role" : "system",
        "content" : "Imagine the detail appeareance of the input., briefly"
    }]
    
    with st.spinner("Waiting for DallE..."):
        DallE_response = openai.Image.create(
            prompt=User_input,
            size="1024x1024"
        )

    st.image(DallE_response["data"][0]["url"])

    GPT_Prompt.append({
        "role" : "system",
        "content" : User_input
    })
    
    with st.spinner("Waiting for ChatGPT..."):
        GPT_response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages=GPT_Prompt
        )
    
    prompt = GPT_response["choices"][0]["message"]["content"]
    st.write(prompt)
