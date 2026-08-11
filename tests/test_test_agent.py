from agents.testing_agent import TestingAgent as Agent
from memory.memory import Memory

def test_tesingt_agent_memory():
  memory=Memory()
  agent=Agent(memory)
  agent.execute("Run unit test")
  assert memory.get("last_test")=="Run unit test"
