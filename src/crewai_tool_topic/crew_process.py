import os
from crewai import Agent, Task, Crew, Process, LLM
from crewai_tools import (
    DirectoryReadTool,
    FileReadTool,
    SerperDevTool,
)

llm1 = LLM(
    model = "gemini/gemini-1.5-flash",
    api_key= "AIzaSyBrojHZPCWGWsvbnFxeBbRRNAyuqYd_x5k"
)

# Instantiate tools
docs_tool = DirectoryReadTool(directory='./blog-posts2')
file_tool = FileReadTool()
search_tool = SerperDevTool()

# Define your agents
researcher = Agent(
    role="Researcher",
    goal="Conduct thorough research and analysis on AI and AI agents",
    backstory="You're an expert researcher, specialized in technology, software engineering, AI, and startups. You work as a freelancer and are currently researching for a new client.",
    allow_delegation=False,
    tools=[search_tool],
    llm=llm1
)

writer = Agent(
    role="Senior Writer",
    goal="Create compelling content about AI and AI agents",
    backstory="You're a senior writer, specialized in technology, software engineering, AI, and startups. You work as a freelancer and are currently writing content for a new client.",
    allow_delegation=False,
    tools=[docs_tool,file_tool],
    llm=llm1
)

# Define your task
task = Task(
    description="Generate a list of 5 interesting ideas for an article, then write one captivating paragraph for each idea that showcases the potential of a full article on this topic. Return the list of ideas with their paragraphs and your notes.",
    expected_output="5 bullet points, each with a paragraph and accompanying notes.",
)

# Define the manager agent
manager = Agent(
    role="Project Manager",
    goal="Efficiently manage the crew and ensure high-quality task completion",
    backstory="You're an experienced project manager, skilled in overseeing complex projects and guiding teams to success. Your role is to coordinate the efforts of the crew members, ensuring that each task is completed on time and to the highest standard.",
    allow_delegation=True,
    llm=llm1
)

# Instantiate your crew with a custom manager
crew = Crew(
    agents=[researcher, writer],
    tasks=[task],
    manager_agent=manager,
    function_calling_llm=llm1,
    process=Process.hierarchical,
    verbose=True

)

# Start the crew's work
def kickoff():
    result = crew.kickoff()