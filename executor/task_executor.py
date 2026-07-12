class TaskExecutor:
  def __init__(self,planner):
    self.planner=planner
  
  def run(self,task):
    selected_agent=self.planner.select_agent(task)
    if selected_agent:
      print(f"Selected Agent: {selected_agent.name}")
      return selected_agent.execute(task)
    else:
      print("Agent Not Found")
