from registry.agent_registry import AgentRegistry
from agents.research_agent import ResearchAgent
from agents.coding_agent import CodingAgent
from agents.testing_agent import TestingAgent
from planner.planner import Planner
from executor.task_executor import TaskExecutor
from shared_state.shared_state import SharedState
from tools.tool_manager import ToolManager

registry=AgentRegistry()
research=ResearchAgent()
coding=CodingAgent()
testing=TestingAgent()

registry.register(research)
registry.register(coding)
registry.register(testing)
planner=Planner(registry)
shared_state=SharedState()
tool_manager=ToolManager()

task="Test login module"

executor=TaskExecutor(planner)

executor.run(task)
