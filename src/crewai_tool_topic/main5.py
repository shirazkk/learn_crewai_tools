# from crewai import Agent, Task, Crew, LLM
# from crewai.tools import tool

# # 🔹 Step 1: Define a Tool to Check Prime Numbers
# @tool
# def is_prime_tool(number: int) -> str:
#     """Checks if a number is prime."""
#     if number < 2:
#         return f"{number} is NOT a prime number."
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             return f"{number} is NOT a prime number."
#     return f"{number} is a PRIME number."

# # 🔹 Step 2: Define the Caching Function
# def prime_cache_function(args, result):
#     # Only cache the result if the number is greater than 10
#     cache = args[0] > 10
#     return cache

# # Apply caching function to the tool
# is_prime_tool.cache_function = prime_cache_function

# # 🔹 Step 3: Define the LLM Model (Replace with Your API Key)
# llm = LLM(
#     model="gemini/gemini-1.5-flash",
#     api_key= "AIzaSyBrojHZPCWGWsvbnFxeBbRRNAyuqYd_x5k"
# )

# # 🔹 Step 4: Create an Agent that Uses This Tool
# math_teacher = Agent(
#     role="Math Teacher",
#     goal="Teach students about prime numbers.",
#     backstory="You are an experienced math teacher, passionate about helping students.",
#     tools=[is_prime_tool],  # Using our tool
#     allow_delegation=False,
#     verbose=True,
#     llm=llm
# )

# # 🔹 Step 5: Define the Task
# prime_check_task = Task(
#     description="A student asked: '{query}'. Use the prime checking tool to respond correctly.",
#     expected_output="A correct statement about the number's primality.",
#     agent=math_teacher,
#     output_file="prime_number.md"
# )

# # 🔹 Step 6: Set Up the Crew
# crew = Crew(
#     agents=[math_teacher],
#     tasks=[prime_check_task],
#     verbose=True
# )

# # 🔹 Step 7: Kickoff and Run
# def kickoff():
#     crew.kickoff(inputs={
#         "query": "Is 13 a prime number?"
#     })
