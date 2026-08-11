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
    self.memory.set("last_research",task)
    last_task=self.memory.get("last_research")
    print(last_task)
    return f"Researching: {task}"
