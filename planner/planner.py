class Planner:
  
  def __init__(self,registry):
    self.registry=registry
  def select_agent(self,task):
    task=task.lower()
    for agent in self.registry.get_agents():
      for capability in agent.capabilities:
        if capability in task:
          return agent
    return None
