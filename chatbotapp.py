from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq

# Create inference server
app = FastAPI()

# Connect to Groq LLM
client = Groq()

# Pydantic request model
class ChatRequest(BaseModel):
    prompt: str


# ----------------------------
# STEP 1: BASIC LLM ENDPOINT
# ----------------------------
@app.post("/chat")
def chat(req: ChatRequest):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": req.prompt}
        ]
    )

    return {
        "reply": response.choices[0].message.content
    }


# ----------------------------
# STEP 2: CHATBOT WITH MEMORY
# ----------------------------
# Conversation memory stored here
chat_history = []

@app.post("/chatbot")
def chatbot(req: ChatRequest):
    global chat_history

    # Add user message to history
    chat_history.append({"role": "user", "content": req.prompt})

    # Call the LLM using full history
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=chat_history
    )

    bot_reply = response.choices[0].message.content

    # Add bot reply to history
    chat_history.append({"role": "assistant", "content": bot_reply})

    return {
        "reply": bot_reply,
        "history": chat_history[-6:]
    }

// uvicorn app:app --reload

// then a url will appear then from here try out and see for endpoints of /chatbot and /chat (raw llm call).
// json prompt for : /chat :  "prompt": "What is an inference server?"
// json prompt for : /chatbot : "prompt": "Hello, who are you?"
to see if it remmebers the previously asked question then do this prompt : "prompt": "What did I just ask you?"
