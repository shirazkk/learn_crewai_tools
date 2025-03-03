# Creating your own Tools

from crewai import Agent, Task, Crew,LLM
from crewai_tool_topic.tools.custom_tool import PiaicStudentCard

llm = LLM(
    model = "gemini/gemini-1.5-flash",
    api_key= "AIzaSyBrojHZPCWGWsvbnFxeBbRRNAyuqYd_x5k"
)


card = PiaicStudentCard()

piaic_manager = Agent(
    role="PIAIC manager",
    goal = "Manage all quries regarding PIAIC and you will use only relevant tools for student query",
    backstory="""You are a master at understanding people and their preferences.""",
    tools=[card],
    verbose=True,
    llm=llm
)

piaic_card_creator = Task(
    description="you will be responsible for all PIAIC relevant operations, student query '{query}' you must be know how to answer his question based on final context",
    expected_output="final query answer only",
    agent=piaic_manager
)

crew = Crew(
    agents=[piaic_manager],
    tasks=[piaic_card_creator],
    verbose=True
)
def kickoff():
    result = crew.kickoff(inputs={
        "query":"I'm PIAIC student my name is Muhammad Qasim and my roll number is 100, can you create my student card."
    })

    print(result)