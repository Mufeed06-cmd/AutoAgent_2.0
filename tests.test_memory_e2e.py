from memory.memory import Memory
from agents.coding_agent import CodingAgent
from agents.testing_agent import TestingAgent
from agents.research_agent import ResearchAgent

def test_memory_end_to_end():
  memory=Memory()
  research=ResearchAgent(memory)
  coding=CodingAgent(memory)
  testing=TestingAgent(memory)
  research.execute("Research wikipedia.")
  coding.execute("Code a hello world program in python.")
  testing.execute("Test a unit case.")
  
  assert memory.get("last_research")=="Research wikipedia."
  assert memory.get("last_task")=="Code a hello world program in python."
  assert memory.get("last_test")=="Test a unit case."
