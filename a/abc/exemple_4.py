from exemple_3 import Parent

class Child(Parent):
    def __init__(self):
        self._parameters = {}

    def get_info(self, parameter):
        return self._parameters.get(parameter)

    def set_info(self, parameter, value):
        self._parameters[parameter] = value
        return self._parameters


c1 = Child()

c1.set_info('name', 'BB-8')
# {'name': 'BB-8'}
