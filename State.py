from abc import ABCMeta, abstractmethod
class State(metaclass=ABCMeta):
    def __init__(self,calculator):
        pass
    @abstractmethod
    def enternum(self,num):
        pass
    @abstractmethod
    def enteroperation(self,operation):
        pass
    @abstractmethod
    def entereq(self):
        pass
