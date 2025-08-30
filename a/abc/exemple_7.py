import abc

# @abc.abstractclassmethod ==

class C(abc.ABC):
    @classmethod
    @abc.abstractmethod
    def my_abstract_classmethod(cls, arg):
        ...

# @abc.abstractstaticmethod ==

class D(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def my_abstract_staticmethod(arg):
        ...
# @abc.abstractproperty ==
class E(abc.ABC):
    @property
    @abc.abstractmethod
    def my_abstract_property(self):
        ...

class F(abc.ABC):
    @property
    def x(self):
        ...

    @x.setter
    @abc.abstractmethod
    def x(self, val):
        ...

class G(F):
    @F.x.setter
    def x(self, val):
        ...