# from crewai import Agent, Task, Crew, LLM
# from crewai_tools import AIMindTool

# # Initialize the tool
# aimind_tool = AIMindTool(
#     datasources=[
#         {
#             "description": "this is sales manager data that contains potential customer details and customer call summaries",
#             "engine": "Demo database",
#             "connection_data": {
#                 "user": "demo_user",
#                 "password": "demo_user",
#                 "host": "samples.mindsdb.com",
#                 "port": 5432,
#                 "database": "Sales_Data_Expert",
#                 "schema": "demo_data"
#             },
#             "tables": ["car_info", "car_sales","financial_headlines"]
#         }
#     ]
# )

# llm = LLM(
#     model="gemini/gemini-1.5-flash",
#     api_key="AIzaSyBrojHZPCWGWsvbnFxeBbRRNAyuqYd_x5k"
# )

# data_analyst = Agent(
#     role="Data Analyst",
#     goal="Analyze sales manager data to identify potential customers and summarize customer calls.",
#     backstory="You are an expert data analyst with a deep understanding of sales data and customer interactions. Your analysis helps in identifying potential customers and summarizing customer call details.",
#     tools=[aimind_tool],
#     llm=llm
# )

# sales_data_analysis = Task(
#     description="Analyze the sales manager data to identify potential customers and summarize customer call details.",
#     expected_output="A comprehensive report detailing potential customers and summarized customer call details, supported by data from the SALES_MANAGER_DATA database.",
#     agent=data_analyst
# )

# crew = Crew(
#     agents=[data_analyst],
#     tasks=[sales_data_analysis],
#     verbose=True,
#     planning=True,
#     planning_llm=llm
# )

# def kickoff():
#     crew.kickoff()