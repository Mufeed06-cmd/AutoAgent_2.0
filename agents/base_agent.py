from abc import ABC, abstractmethod

class BaseAgent(ABC):
  def __init__(self,name,description,capabilities,tools,memory):
    self.name=name
    self.description=description
    self.capabilities=capabilities
    self.tools=tools
    self.memory=memory
  @abstractmethod
  def execute(self,task):
    pass
