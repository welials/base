import abc

class Parent(abc.ABC):
    @abc.abstractmethod
    def get_info(self, parameter):
        """Get parameter info"""

    @abc.abstractmethod
    def set_info(self, parameter, value):
        """Set parameter to value"""

# Нельзя создать экземпляр класса Parent

parent = Parent()
"""
TypeError: Can't instantiate abstract class Parent without an 
implementation for abstract methods 'get_info', 'set_info'
"""