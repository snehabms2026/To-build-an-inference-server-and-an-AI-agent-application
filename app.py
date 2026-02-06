from fastapi import FastAPI
from groq import Groq

# Create the inference server
app = FastAPI()

# Connect to Groq LLM
client = Groq()

# API endpoint
@app.post("/chat")
def chat(prompt: str):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",  //llama3 models run on groq gpus
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return {
        "reply": response.choices[0].message.content
    }

//We will run an LLM via Groq → wrap it with a small Python server → expose it as an API → call it like a chatbot/agent
//This is literally what “build your own inference server” means (at screening level).

Flow of the project:

1. to install the required libraries via terminal:
//pip install fastapi uvicorn groq
FastAPI → creates APIs
Uvicorn → runs the server
Groq → talks to LLMs (Llama3, Mixtral)

2. to go to groq console, create groq api and copy to the cli.
// setx GROQ_API_KEY "PASTE_YOUR_KEY_HERE"
after this restart, VS code.

3. then create a new file app.py in the screening folder and paste the aboce mentioned code.
  
4.Now go to terminal and run the command as follows to run the inference server:
// uvicorn app:app --reload

5. //Uvicorn running on http://127.0.0.1:8000 , till u see this in the terminal fix the issuses with either groq api key(2) or save the app.py with necessary changes.

6. once u open this in the browser u shuld be able to see a swagger UI(u get this automatically thru fastapi we created in app.py).

7. open the swagger ui, click on post/create then try it out and give the string "Explain what an inference server is in one line" inside the dialogue box of prompt.
// @app.post("/chat")
Detects /chat
Knows it is a POST API
Knows it takes a prompt string
Lets you send requests without writing extra code

8.Your API function is: def chat(prompt: str)
//The API expects one string
  Swagger already knows the type is string
  Swagger automatically wraps it correctly
so no json.

9. if this is a success : we see in terminl 200  OK status code and on the swagger UI interface rendered we can see the response.

10.If anything breaks, do the changes and crtl + C to abort the currently running process in terminal and then use this to reload // uvicorn app:app --reload.
  





