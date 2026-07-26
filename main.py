from registry.agent_registry import AgentRegistry
from agents.research_agent import ResearchAgent
from agents.coding_agent import CodingAgent
from agents.testing_agent import TestingAgent
from planner.planner import Planner
from executor.task_executor import TaskExecutor
from shared_state.shared_state import SharedState
from tools.tool_manager import ToolManager
from response_builder.response_builder import ResponseBuilder

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
Response=ResponseBuilder()

task="Research Multi Agent System and Write small code on it."

executor=TaskExecutor(planner,shared_state)

response=executor.run(task)
result=Response.build(response)
print(result)
