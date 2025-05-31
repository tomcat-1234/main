


class Node:

  def __init__(this,f):
    print("__init__")
    this.f=f
    
  def __call__(this):
    print("Starting Wrapped Function")
    this.f()
    print("Completed Wrapped Function")


@Node
def function1():
  print("Production Function")
  


function1()

