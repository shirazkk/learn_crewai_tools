from crewai import Agent, Task , Crew , LLM
from crewai_tools import (
    DirectoryReadTool,
    FileReadTool,
    SerperDevTool,
)

llm = LLM(
    model = "gemini/gemini-1.5-flash",
    api_key= "AIzaSyBrojHZPCWGWsvbnFxeBbRRNAyuqYd_x5k"
)
SERPER_API_KEY = "d075961daf71a73f9079ec55f5624968224bfc76"



doc_tool = DirectoryReadTool(directory='./blog-posts')
file_tool = FileReadTool()
serper_tool = SerperDevTool()

cricket_analyst = Agent(
    role="Cricket Analyst",
    goal="Research and identify the best cricket player of 2024 using real-world data.",
    backstory="You are a seasoned cricket analyst with expertise in evaluating player performances based on match statistics, expert opinions, and historical data. Your insights are backed by extensive research from reliable online sources.",
    tools=[serper_tool],
    llm=llm
)

cricket_blogger = Agent(
    role="Cricket Blogger",
    goal="Write an engaging and fact-based blog post about the top cricket player of 2024.",
    backstory="You are a passionate cricket journalist specializing in performance analysis, match reviews, and storytelling. Your writing is both informative and entertaining for cricket fans.",
    tools=[doc_tool, file_tool],
    llm=llm
)

player_research  = Task(
    description="Gather the latest match statistics, expert reviews, and rankings to determine the best-performing cricket player of 2024.",
    expected_output="A well-structured report listing the top cricket player of 2024, supported by real match statistics, rankings, and expert insights.",
    agent=cricket_analyst
)

blog_writer = Task(
    description="Based on the research from the Cricket Analyst, craft a well-structured blog post highlighting the achievements, statistics, and impact of the best cricket player of 2024",
    expected_output=""""
    A markdown-formatted blog post including:
        Introduction (context of the 2024 season)
        Player Profile (background, strengths)
        Statistical Breakdown (batting/bowling averages, match performances)
        Conclusion (why they stand out in 2024)
    """,
    agent=cricket_blogger,
    output_file="blog-posts/cricket_player_2024.md"
)

crew = Crew(
    agents=[cricket_analyst, cricket_blogger],
    tasks=[player_research, blog_writer],
    verbose = True,
    planning= True,
    planning_llm=llm
)


def kickoff():
    crew.kickoff()