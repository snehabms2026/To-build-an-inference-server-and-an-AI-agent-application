from simple_agent.crew import SimpleAgent

if __name__ == "__main__":
    crew = SimpleAgent()
    result = crew.crew().kickoff(
        inputs={"topic": "What is an inference server?"}
    )
    print("\nFinal Output:\n", result)
