# # import os
# # from crewai import Agent, Task, Crew, LLM
# # from crewai_tools import DallETool

# # llm = LLM(
# #     model = "gemini/gemini-1.5-flash",
# #     api_key= "AIzaSyBrojHZPCWGWsvbnFxeBbRRNAyuqYd_x5k"
# # )


# # image_tool = DallETool()  # To generate images using DALL·E


# # # # Agent 1: Researcher (Finds and describes image concepts)
# # # researcher = Agent(
# # #     role="AI Image Researcher",
# # #     goal="Gather detailed information and creative prompts for AI-generated images.",
# # #     backstory="An expert in AI-generated art with deep knowledge of artistic styles, compositions, and creative trends.",
# # #     tools=[image_tool],
# # #     llm=llm
# # # )

# # # Agent 2: Image Generator (Uses DALL·E to create images)
# # image_creator = Agent(
# #     role="AI Image Creator",
# #     goal="Generate high-quality image of cat",
# #     backstory="A cutting-edge AI-driven artist who transforms text descriptions into stunning AI-generated visuals.",
# #     tools=[image_tool],
# #     llm=llm
# # )

# # # Task 1: Research and Describe Image
# # # research_task = Task(
# # #     description="Research trending AI-generated art concepts and provide a detailed prompt for generating a high-quality image.",
# # #     expected_output="A creative and detailed text prompt suitable for AI image generation, covering style, colors, lighting, and composition.",
# # #     agent=researcher
# # # )

# # # Task 2: Generate Image using DALL·E
# # image_task = Task(
# #     description="Use DALL·E to generate a stunning AI image",
# #     expected_output="A high-resolution AI-generated image",
# #     agent=image_creator,
# #     output_file="generated_images/ai_art.png"
# # )

# # # Create Crew
# # crew = Crew(
# #     agents=[image_creator],
# #     tasks=[ image_task],
# #     verbose=True,
# #     planning=True,
# #     planning_llm=llm
# # )
# # def kickoff():
# #     crew.kickoff()




# import os
# from crewai import Agent, Task, Crew, LLM
# from google.cloud import aiplatform

# # Set up Google Vertex AI
# aiplatform.init(project="sound-inkwell-452620-u1")

# llm = LLM(
#     model="gemini/gemini-1.5-flash",
#     api_key="AIzaSyBrojHZPCWGWsvbnFxeBbRRNAyuqYd_x5k"
# )

# # Google Image Generation Tool
# class GoogleImageTool:
#     def generate_image(self, prompt):
#         response = aiplatform.generation.generate_text(
#             model="imagen",
#             prompt=prompt
#         )
#         return response

# image_tool = GoogleImageTool()  # Replace DALL·E with Google AI

# # Agent: Image Generator (Uses Google AI to create images)
# image_creator = Agent(
#     role="AI Image Creator",
#     goal="Generate high-quality images using Google AI",
#     backstory="A cutting-edge AI-driven artist who transforms text descriptions into stunning AI-generated visuals.",
#     tools=[image_tool],  # Using Google AI instead of DALL·E
#     llm=llm
# )

# # Task: Generate Image using Google AI
# image_task = Task(
#     description="Use Google's AI to generate a stunning AI image of a cat.",
#     expected_output="A high-resolution AI-generated image",
#     agent=image_creator,
#     output_file="generated_images/ai_art.png"
# )

# # Create Crew
# crew = Crew(
#     agents=[image_creator],
#     tasks=[image_task],
#     verbose=True,
#     planning=True,
#     planning_llm=llm
# )

# def kickoff():
#     crew.kickoff()
