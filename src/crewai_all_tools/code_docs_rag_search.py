from crewai import Agent, Task, Crew, LLM
from crewai_tools import CodeDocsSearchTool

llm = LLM(
    model="gemini/gemini-1.5-flash",
    api_key="AIzaSyBrojHZPCWGWsvbnFxeBbRRNAyuqYd_x5k"
)

# 1. Initialize the documentation search tool for the Requests library docs
requests_docs_url = "https://realpython.com/python-requests/"
docs_tool = CodeDocsSearchTool(
    docs_url=requests_docs_url,
        config=dict(
        llm=dict(
            provider="google",  # or google, openai, anthropic, llama2, ...
            config=dict(
                model="gemini/gemini-2.0-flash",
                # stream=True,
                # temperature=0.5,
                # top_p=1,
            ),
        ),
        embedder=dict(
            provider="google",  # or openai, ollama, ...
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
                title="Embeddings",
            ),
        ),
    )
)
question = "How do I send a GET request with a custom header using the Requests library?"

# 2. Create an agent with the role of a documentation assistant, including the tool
doc_agent = Agent(
    role="Requests Docs Assistant",
    goal=question,
    backstory= 'You are experinced python programmer assistant with 5 years of experince',
    llm=llm,
    tools=[docs_tool]
)


task = Task(agent=doc_agent, expected_output= 'implemention of requests in python', description="Answer the question using documentation")

# 4. Create a Crew with the agent and the task, using a sequential process
crew = Crew(agents=[doc_agent], tasks=[task], verbose=True,planning=True,planning_llm=llm)

# 5. Run the Crew to execute the task
def kickoff():
    crew.kickoff()


if __name__ == "__main__":
    kickoff()














# from crewai_tools import CodeDocsSearchTool
# from crewai import Agent, Task, Crew, LLM

# llm = LLM(
#     model="gemini/gemini-1.5-flash",
#     api_key="AIzaSyBrojHZPCWGWsvbnFxeBbRRNAyuqYd_x5k"
# )

# tool = CodeDocsSearchTool(
#     docs_url=('https://sports.ndtv.com/cricket/icc-rankings/odi-batting'),
#     config=dict(
#         llm=dict(
#             provider="google",  # or google, openai, anthropic, llama2, ...
#             config=dict(
#                 model="gemini/gemini-1.5-flash",
#                 # stream=True,
#                 # temperature=0.5,
#                 # top_p=1,
#             ),
#         ),
#         embedder=dict(
#             provider="google",  # or openai, ollama, ...
#             config=dict(
#                 model="models/embedding-001",
#                 task_type="retrieval_document",
#                 title="Embeddings",
#             ),
#         ),
#     )
# )

# cricket_analyst = Agent(
#     role="Cricket Analyst",
#     goal="Research and identify the best cricket player of 2025 using real-world data.",
#     backstory="You are a seasoned cricket analyst with expertise in evaluating player performances based on match statistics, expert opinions, and historical data. Your insights are backed by extensive research from reliable online sources.",
#     tools=[tool],
#     llm=llm
# )

# player_research = Task(
#     description="Gather the latest match statistics, expert reviews, and rankings to determine the best-performing cricket player of 2025.",
#     expected_output="A well-structured report listing the top cricket player of 2025, supported by real match statistics, rankings, and expert insights.",
#     agent=cricket_analyst
# )

# crew = Crew(
#     agents=[cricket_analyst],
#     tasks=[player_research],
#     verbose=True,
#     planning=True,
#     planning_llm=llm
# )

# def kickoff():
#     crew.kickoff()


# if __name__ == "__main__":
#     kickoff()


