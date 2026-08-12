from memory.memory import Memory
from agents.coding_agent import CodingAgent
from agents.research_agent import ResearchAgent
from agents.testing_agent import TestingAgent


def test_memory_end_to_end():
    memory = Memory()

    research = ResearchAgent(memory)
    coding = CodingAgent(memory)
    testing = TestingAgent(memory)

    research.execute("Research Python")
    coding.execute("Write Python code")
    testing.execute("Test Python code")

    assert memory.get("last_research") == "Research Python"
    assert memory.get("last_task") == "Write Python code"
    assert memory.get("last_test") == "Test Python code"
