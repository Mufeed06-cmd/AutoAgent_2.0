from agents.research_agent import ResearchAgent
from memory.memory import Memory

def test_research():
  memory=Memory()
  agent=ResearchAgent(memory)
  agent.execute("Research the stack overflow.")
  assert memory.get("last_research")=="Research the stack overflow."
