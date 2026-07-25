class Planner:

    def __init__(self, registry):
        self.registry = registry

    def decompose_task(self, task):
        # Normalize input
        task = task.lower()

        # Convert different separators into "and"
        task = task.replace(" then ", " and ")
        task = task.replace(",", " and ")

        # Split into subtasks
        subtasks = task.split(" and ")

        # Remove empty or whitespace-only subtasks
        clean_subtasks = []
        for subtask in subtasks:
            if subtask.strip() != "":
                clean_subtasks.append(subtask.strip())

        return clean_subtasks

    def select_agent(self, task):
        task_plan = {}
        subtasks = self.decompose_task(task)

        for subtask in subtasks:
            agents_for_subtask = []

            for agent in self.registry.get_agents():
                for capability in agent.capabilities:
                    if capability in subtask and agent not in agents_for_subtask:
                        agents_for_subtask.append(agent)

            # Keep the subtask even if no agent is found
            task_plan[subtask] = agents_for_subtask

        return task_plan
