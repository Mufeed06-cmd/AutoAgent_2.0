from .base_agent import BaseAgent

class ResearchAgent(BaseAgent):
  def __init__(self,memory):
    super().__init__(
name="Research Agent",
description="Searches and analyzes information",
capabilities=["research","analysis"],
tools=[],
memory=memory
)
  def execute(self,task):
    return f"Researching: {task}"
