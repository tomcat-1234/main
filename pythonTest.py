


class Node:

  def __init__(this,arg):
    print("__init__")

  def __call__(self,f):
    print("Starting Wrapped Function")
    f()
    print("Completed Wrapped Function")


@Node
def function1():
  print("Production Function")
  


function1()

