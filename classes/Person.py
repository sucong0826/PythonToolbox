# Person class
# It is just a practice

class Person:
    """ Class to represent a person"""

    token = ""

    def __init__(self, name = '', age = 0):
          self.__name = name
          self.__age = age

    def display(self):
          print("Person(%s, %d)" % (self.name, self.age))

    @property
    def age(self):
          return self.__age

    @property
    def name(self):
          return self.__name

    @age.setter
    def age(self, age):
        if(0 < age < 150):
            self.__age = age

    @name.setter
    def name(self, name):
        if(name == ''):
            return
        self.__name = name
