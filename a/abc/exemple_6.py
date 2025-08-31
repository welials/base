import abc


class C(abc.ABC):
    @abc.abstractmethod
    def my_abstract_method(self, arg1):
        ...
    @classmethod
    @abc.abstractmethod
    def my_abstract_classmethod(cls, arg2):
        ...
    @staticmethod
    @abc.abstractmethod
    def my_abstract_staticmethod(arg3):
        ...

    @property
    @abc.abstractmethod
    def my_abstract_property(self):
        ...
    @my_abstract_property.setter
    @abc.abstractmethod
    def my_abstract_property(self, val):
        ...

    @abc.abstractmethod
    def _get_x(self):
        ...
    @abc.abstractmethod
    def _set_x(self, val):
        ...
    x = property(_get_x, _set_x)

class Descriptor:
    ...
    @property
    def __isabstractmethod__(self):
        return any(getattr(f, '__isabstractmethod__', False) for
                   f in (self._fget, self._fset, self._fdel))

