import streamlit as st
import requests
import base64
from collections import deque

st.title("Text to Speech App powered by Gradio API hosted on 🤗")

# Initialize the last_five_inputs list in the st.session_state dictionary
if 'last_five_inputs' not in st.session_state:
    st.session_state.last_five_inputs = deque(maxlen=5)

inp_text = st.text_input("Enter your text here.....")

button = st.button("⚡️ Text to speech magic ⚡️")

if button:

    with st.spinner():

        response_json = requests.post("https://abidlabs-speak.hf.space/run/predict", json={
        "data": [
            inp_text,
        ]}).json()

        # Append the input text to the last_five_inputs list in st.session_state
        st.session_state.last_five_inputs.append(inp_text)

        md = f"""
            <audio controls>
            <source src="{response_json['data'][0]}" type="audio/flac">
            </audio>
            """
        st.markdown(md, unsafe_allow_html=True)

# Show the last 5 input texts
if st.session_state.last_five_inputs:
    st.write("Last 5 input texts:")
    for i, inp in enumerate(st.session_state.last_five_inputs):
        st.write(f"{i+1}. {inp}")
