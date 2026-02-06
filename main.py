#!/usr/bin/env python
from simple_agent.crew import SimpleAgent
from datetime import datetime

def run():
    inputs = {
        "topic": "What is an inference server?",
        "current_year": str(datetime.now().year)
    }

    result = SimpleAgent().crew().kickoff(inputs=inputs)
    print("\nFinal Output:\n", result)
