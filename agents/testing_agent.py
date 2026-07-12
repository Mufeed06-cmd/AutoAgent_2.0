from .base_agent import BaseAgent

class TestingAgent(BaseAgent):
  def __init__(self):
    super().__init__(
name="Testing Agent",
description="Tests Software",
capabilities=["test","validate"],
tools=[]
)
  def execute(self,task):
    return f"Testing: {task}"
