"""
abstractclassmethod
Не рекомендуется, начиная с версии 3.3:
Теперь можно использовать classmethod с abstractmethod(),
что делает данный декоратор избыточным.
"""
from abc import abstractmethod, ABC


class C(ABC):
    @classmethod
    @abstractmethod
    def my_abstract_classmethod(cls):
        pass