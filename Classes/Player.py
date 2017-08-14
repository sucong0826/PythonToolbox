# player class
class Player:
     def __init__(self, name):
          self.__name = name
          self.__score = 0

     def reset_score(self):
          self.__score = 0

     def increase_score(self):
          self.__score = self.__score + 1

     def get_name(self):
          return self.__name

     def __str__(self):
          return "name = '%s', score = %d" % (self.__name, self.__score)

     def __repr__(self):
          return 'Player(%s)' %  str(self)
