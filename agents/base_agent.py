from abc import ABC, abstractmethod

class BaseAgent(ABC):
  def __init__(self,name,description,capabilities,tools):
    self.name=name
    self.description=description
    self.capabilities=capabilities
    self.tools=tools
  @abstractmethod
  def execute(self,task):
    pass
