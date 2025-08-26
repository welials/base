"""
abstractproperty
Не рекомендуется, начиная с версии 3.3:
Теперь можно использовать property, property.getter(), property.setter() и property.deleter() с abstractmethod(),
что делает данный декоратор избыточным.
"""
from abc import abstractmethod, ABC

"""
чтение
"""

class C(ABC):
    @property
    @abstractmethod
    def my_abstract_property(self):
        pass
"""
чтение-запись
"""

class D(ABC):
    @property
    def x(self):
        pass

    @x.setter
    @abstractmethod
    def x(self, val):
        pass

"""
Если только некоторые компоненты являются абстрактными, 
только данные компоненты необходимо обновить, 
чтобы создать свойство в подклассе:
"""
class E(D):
    @C.x.setter
    def x(self, val):
        pass