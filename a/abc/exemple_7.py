import abc

# @abc.abstractclassmethod ==

class C(abc.ABC):
    @classmethod
    @abc.abstractmethod
    def my_abstract_classmethod(cls, arg):
        ...