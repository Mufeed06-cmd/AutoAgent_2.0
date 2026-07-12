from .base_agent import BaseAgent

class CodingAgent(BaseAgent):
  def __init__(self):
    super().__init__(
name="Coding Agent",
description="Writes and modifies code",
capabilities=["code","debug","refactor"],
tools=[]
)
  def execute(self,task):
    return f"Coding: {task}"
