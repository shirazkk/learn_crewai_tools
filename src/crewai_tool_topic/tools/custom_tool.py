from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type

class MyToolConfig(BaseModel):
    """Input schema for MyCustomTool."""
    student_name: str = Field(..., description="Student name")
    student_roll_no : int = Field(..., description="student id")

class PiaicStudentCard(BaseTool):
    name: str = "Piaic student card generator"
    description: str = "this function will create Piaic student card"
    args_schema: Type[BaseModel] = MyToolConfig

    def _run(self, student_name:str,student_roll_no:int)->str:
        return f"""PIAIC student card
    student name: {student_name}
    student roll no: {student_roll_no}
    Pakistan zindabd!
            """

