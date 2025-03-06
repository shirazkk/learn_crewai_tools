from crewai import Agent, Task, Crew, Process,LLM
from crewai_tools import CodeInterpreterTool
import os

API_KEY=os.getenv("GOOGLE_API_KEY")
llm=LLM(
    model="gemini/gemini-1.5-flash",
    api_key=API_KEY
)

# Initialize the tool
code_interpreter = CodeInterpreterTool()

# Define an agent that uses the tool
programmer_agent = Agent(
    role="Python Programmer",
    goal="Write and execute Python code to solve problems",
    backstory="An expert Python programmer who can write efficient code to solve complex problems.",
    tools=[code_interpreter],
    verbose=True,
    llm=llm
)

# Example task to generate and execute code
coding_task = Task(
    description="Write a Python function to calculate the Fibonacci sequence up to the 10th number and print the result.",
    expected_output="The Fibonacci sequence up to the 10th number.",
    agent=programmer_agent,
)

# Create and run the crew
crew = Crew(
    agents=[programmer_agent],
    tasks=[coding_task],
    verbose=True,
    process=Process.sequential,
)
def kickoff():      
    crew.kickoff()