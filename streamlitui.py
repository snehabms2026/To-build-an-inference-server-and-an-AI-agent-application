import streamlit as st
import requests

# ---------------------------
# FastAPI Backend URL
# ---------------------------
BACKEND_URL = "http://127.0.0.1:8000/chatbot"

# ---------------------------
# Streamlit Page Setup
# ---------------------------
st.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="centered")

st.title("🤖 AI Chatbot — AMD Agent Screening")
st.write("Ask me anything!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Input box for user
user_input = st.chat_input("Type your message...")

if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Show user message immediately
    with st.chat_message("user"):
        st.write(user_input)

    # Call FastAPI backend
    try:
        response = requests.post(
            BACKEND_URL,
            json={"prompt": user_input},
            timeout=20
        )

        bot_reply = response.json().get("reply", "Error: No reply from server.")

    except Exception as e:
        bot_reply = f"❌ Error communicating with backend: {e}"

    # Add bot reply to history
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

    # Show bot reply
    with st.chat_message("assistant"):
        st.write(bot_reply)

// C:\Users\samru\amd_agent_screening> pip install streamlit requests (u shuld kee the backend running w)
//docker run -p 8000:8000 --env-file .env amd-inference-server, u get : Backend docs → http://127.0.0.1:8000/docs : swagger shuld open with status code 200 OK
// streamlit run streamlit_app.py : http://localhost:8501 : u see the interface(later can deploy, rn its local)
