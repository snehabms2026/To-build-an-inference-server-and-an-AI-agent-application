We will run an LLM via Groq → wrap it with a small Python server → expose it as an API → call it like a chatbot/agent
//This is literally what “build your own inference server” means (at screening level).

C:\Users\samru\
├── amd_agent_screening\
│   └── app.py   (FastAPI + inference)
│
└── crewai_agent\
    └── venv

//for building the agent 

1. keep app.py folder separetely then creat a new folder called crewai_agent through the terminal using:
   cd.. go to root first then //mkdir crewai_agent
                              //cd crewai_agent
   C:\Users\samru\
├── amd_agent_screening   ← inference server (finished)
└── crewai_agent          ← CrewAI agent app (new)
//PS C:\Users\samru\crewai_agent>
//python -m venv venv
//venv\Scripts\activate
//(venv) PS C:\Users\samru\crewai_agent>

2. //pip install crewai crewai-tools groq python-dotenv

3. crewai create crew simple_agent
// let crewai know ur llm provider and then later give the same API key you gave for ur inference server

4. cd simple_agent then // code .

5. In the new window: simple_agent → src → simple_agent → config = edit agent.yaml and tasks.yaml along with crew.py and main.py

6. Before running, confirm these are aligned:
  agents.yaml contains: explainer_agent
  tasks.yaml contains: explain_task using explainer_agent
  crew.py has methods: explainer_agent() and explain_task()

7.In main.py , kickoff() is significant becoz inputs → tasks → agent → LLM → output (read in detail) : crewai does this pipeline.

8.



 ..after installing venv : it should contain the below files:
 agents.yaml
 tasks.yaml
 crew.py
 main.py  

