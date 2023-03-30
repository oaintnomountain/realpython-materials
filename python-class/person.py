# Setters and getters
# class Person:
#     def __init__(self, name):
#         self.set_name(name)

#     def name(self):
#         return self._name

#     def set_name(self, value):
#         self._name = value


# Property
class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value.upper()
