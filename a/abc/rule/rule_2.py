"""
abstractstaticmethod
Не рекомендуется, начиная с версии 3.3: Теперь можно использовать
staticmethod с abstractmethod(),
что делает данный декоратор избыточным.
"""
from abc import abstractmethod, ABC


class C(ABC):
    @staticmethod
    @abstractmethod
    def my_abstract_staticmethod():
        pass