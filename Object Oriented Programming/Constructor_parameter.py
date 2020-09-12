# This program shows how to pass arguments to a parameterized constructor.

class Another:
  def __init__(self, a, b):  # Parameterized constructor. 
    self.a = a 
    self.b = b
    
  def add(self):
    print('The addition of {} and {} is {}'.format(a, b, a+b))
    
    
obj = Another(10,20) # Passing 10 and 20 to the Another class constructor.
obj.add()            # Calling the add method in Another class.
