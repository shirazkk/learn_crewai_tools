# Creating your own Tools

from crewai import Agent, Task, Crew, LLM
from crewai_tool_topic.tools.password import PasswordStrengthChecker

llm = LLM(
    model="gemini/gemini-1.5-flash",
    api_key="AIzaSyBrojHZPCWGWsvbnFxeBbRRNAyuqYd_x5k"
)

# Importing Password Strength Checker tool
password_checker = PasswordStrengthChecker()

# Creating the Password Security Agent
password_security_agent = Agent(
    role="Cybersecurity Specialist",
    goal="Analyze password strength and provide security recommendations.",
    backstory=(
        "You are an expert in cybersecurity and password security. "
        "You analyze passwords for vulnerabilities and suggest improvements to enhance security."
    ),
    tools=[password_checker],  # ✅ Only using PasswordStrengthChecker
    verbose=True,
    llm=llm
)

# Task for checking password security
password_security_task = Task(
    description=(
        "Evaluate the provided password using the 'PasswordStrengthChecker' tool. "
        "Analyze its strength and provide an assessment such as Weak, Moderate, or Strong. "
        "Suggest security improvements like increasing length, adding special characters, and avoiding common words."
    ),
    expected_output="A detailed password security report with improvement suggestions.",
    agent=password_security_agent
)

# Crew setup with only the Password Security Agent
crew = Crew(
    agents=[password_security_agent],
    tasks=[password_security_task],  # ✅ Only the password security task
    verbose=True
    
)

# Function to kickoff CrewAI execution
def kickoff():
    result = crew.kickoff(inputs={
        "password": "WeakPass1"  # ✅ Example password input
    })

    print(result)
