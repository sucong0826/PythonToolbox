# closure and anonymous functions
def f(x):
     def g(y):
          return x + y
     return g

def h(x):
     return lambda y: x + y

x = 0

def trans(y):
     return x + y

def g(z):
     x = 1
     return trans(z)

