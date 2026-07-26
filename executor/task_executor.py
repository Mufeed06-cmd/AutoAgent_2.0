class TaskExecutor:
    def __init__(self, planner,shared_state):
        self.planner = planner
        self.shared_state=shared_state
        
    def run(self, task):
        response = []
        selected_agent = self.planner.select_agent(task)

        if selected_agent:
            for subtask, agents in selected_agent.items():
                for agent in agents:
                    try:
                      result = agent.execute(subtask)
                      self.shared_state.set(subtask,result)
                      response.append(result)
                    except Exception as e:
                      print(f"Error while executing {agent.name}: {e}")
                      response.append(f"Error while executing {agent.name}: {e}")

            return response
        else:
            print("Agent Not Found")
