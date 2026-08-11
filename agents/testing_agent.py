from .base_agent import BaseAgent

class TestingAgent(BaseAgent):
  def __init__(self,memory):
    super().__init__(
name="Testing Agent",
description="Tests Software",
capabilities=["test","validate"],
tools=[],
memory=memory
)
  def execute(self,task):
    self.memory.set("last_test",task)
    print(self.memory.get("last_test"))
    return f"Testing: {task}"
