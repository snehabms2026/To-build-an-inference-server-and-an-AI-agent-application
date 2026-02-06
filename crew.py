//change @task and @agent

from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, task, crew


@CrewBase
class SimpleCrew:

    @agent
    def explainer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["explainer_agent"],
            verbose=True
        )

    @task
    def explain_task(self) -> Task:
        return Task(
            config=self.tasks_config["explain_task"]
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[self.explainer_agent()],
            tasks=[self.explain_task()],
            verbose=True
        )
