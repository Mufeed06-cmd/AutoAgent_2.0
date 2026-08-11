from .base_agent import BaseAgent

class CodingAgent(BaseAgent):
  def __init__(self,memory):
    super().__init__(
name="Coding Agent",
description="Writes and modifies code",
capabilities=["code","debug","refactor"],
tools=[],
memory=memory
)
  def execute(self,task):
    self.memory.set("last_task",task)
    saved_task=self.memory.get("last_task")
    print(saved_task)
    return f"Coding: {task}"
   
