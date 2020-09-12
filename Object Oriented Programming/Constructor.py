# This program shows the use of constructor without any parameters.

class MyClass:
  def __init__(self):
    print('I am in constructor')
   
  def hello(self):
    print('I am in hello method')
    
obj = MyClass() # Creating an object reference to MyClass class which invokes the default constructor.
obj.hello() # Calling the hello method in the MyClass class.

    
