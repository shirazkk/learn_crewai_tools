
import re
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type

class PasswordStrengthConfig(BaseModel):
    """Input schema for Password Strength Checker."""
    password: str = Field(..., description="Password to check strength")

class PasswordStrengthChecker(BaseTool):
    name: str = "Password Strength Checker"
    description: str = "Analyzes password strength and provides security tips"
    args_schema: Type[BaseModel] = PasswordStrengthConfig

    def _run(self, password: str) -> str:
        score = 0
        suggestions = []

        if len(password) >= 12:
            score += 1
        else:
            suggestions.append("Use at least 12 characters for better security.")

        if re.search(r"[A-Z]", password):
            score += 1
        else:
            suggestions.append("Include uppercase letters.")

        if re.search(r"[a-z]", password):
            score += 1
        else:
            suggestions.append("Include lowercase letters.")

        if re.search(r"[0-9]", password):
            score += 1
        else:
            suggestions.append("Include numbers.")

        if re.search(r"[@$!%*?&]", password):
            score += 1
        else:
            suggestions.append("Use special characters (@, $, !, %, etc.).")

        if score >= 4:
            return "✅ Strong password! Good job!"
        else:
            return "🔍 Password Improvement Suggestions:\n- " + "\n- ".join(suggestions)
