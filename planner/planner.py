class Planner:
  
  def __init__(self,registry):
    self.registry=registry
  def decompose_task(self,task):
    return [task]
  def select_agent(self,task):
    task_plan={}
    subtasks=self.decompose_task(task)
    for subtask in subtasks:
      subtask=subtask.lower()
      agents_for_subtask=[]
      for agent in self.registry.get_agents():
        for capability in agent.capabilities:
          if capability in subtask and agent not in selected_agents:
            agents_for_subtask.append(agent)
            task[subtask]=agents_for_subtask

    return task_plan
