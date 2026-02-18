import os 
from google import genai
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# load api key
os.environ['GOOGLE_API_KEY'] = os.getenv('gemini_key')

# initialize client once in session_state
if 'client' not in st.session_state:
    st.session_state.client = genai.Client()

client = st.session_state.client

system_prompt = 'you are Career Advisor Chatbot, answer the user queries in below 7 sentences with clear and latest advises.'

st.title('Career Advisor Chatbot')

st.write('Type you question in the chat box:')

# initialize chat session only once
if 'chat_session' not in st.session_state:
    st.session_state.chat_session = client.chats.create(
        model = 'gemini-2.5-flash',
        config = genai.types.GenerateContentConfig(
            system_instruction = system_prompt
        )
    )

if 'messages' not in st.session_state:
    st.session_state.messages = []

print(st.session_state)


# display past messages
for role,text in st.session_state.messages:
    if role == 'user':
        st.markdown(f"**you:**{text}")
    else:
        st.markdown(f"**Bot**{text}")

# chat input
user_input = st.chat_input('Type your msg here..')

if user_input:
    st.session_state.messages.append(('user',user_input))

    # send message safely
    chat = st.session_state.chat_session
    response = chat.send_message(user_input)

    bot_reply = response.text
    st.session_state.messages.append(('bot',bot_reply))
    st.rerun()