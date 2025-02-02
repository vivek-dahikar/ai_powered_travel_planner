import yaml
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

with open("config/agents.yaml", "r") as file:
    agents_config = yaml.safe_load(file)

with open("config/tasks.yaml", "r") as file:
    tasks_config = yaml.safe_load(file)

@CrewBase
class AiPoweredTravelPlanner():
    """AI-Powered Travel Planner Crew"""

    @agent
    def travel_researcher(self) -> Agent:
        return Agent(
            config=agents_config['travel_researcher'],
            verbose=True
        )

    @agent
    def food_guide(self) -> Agent:
        return Agent(
            config=agents_config['food_guide'],
            verbose=True
        )

    @agent
    def itinerary_planner(self) -> Agent:
        return Agent(
            config=agents_config['itinerary_planner'],
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=tasks_config['research_task'],
            agent=self.travel_researcher(),
        )

    @task
    def food_task(self) -> Task:
        return Task(
            config=tasks_config['food_task'],
            agent=self.food_guide(),
        )

    @task
    def itinerary_task(self) -> Task:
        return Task(
            config=tasks_config['itinerary_task'],
            agent=self.itinerary_planner(),
            output_file='itinerary.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the AI-Powered Travel Planner Crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
