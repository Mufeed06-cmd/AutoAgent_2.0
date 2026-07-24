class TaskExecutor:
  def __init__(self,planner):
    self.planner=planner
  
  def run(self,task):
    response=[]
    selected_agent=self.planner.select_agent(task)
    if selected_agent:
      for agent in selected_agent:
        print(f"Selected Agent: {agent.name}")
        response.append(agent.execute(task))
      return  response
    else:
      print("Agent Not Found")
