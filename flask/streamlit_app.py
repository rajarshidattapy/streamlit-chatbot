import streamlit as st
import requests

# URL to your Flask API
API_URL = "http://127.0.0.1:5000/chat"

st.title("Chat with Google Gemini")

if 'chat' not in st.session_state:
    st.session_state.chat = None

# Input box for user prompt
prompt = st.chat_input("What can I do for you?")

# Send user input to the backend and display the response
if prompt:
    st.chat_message("user").markdown(prompt)

    # Send request to Flask API
    response = requests.post(API_URL, json={"prompt": prompt, "chat": st.session_state.chat})

    # Process response from the API
    if response.status_code == 200:
        data = response.json()
        st.session_state.chat = data["chat"]
        st.chat_message("assistant").markdown(data["response"])
    else:
        st.error("Something went wrong! Please try again.")
