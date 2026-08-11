from agents.coding_agent import CodingAgent
from memory.memory import Memory

def test_CodingAgent():
  memory=Memory()
  agent=CodingAgent(memory)
  agent.execute("Build login Api")
  
  assert memory.get("last_task")=="Build login Api"
