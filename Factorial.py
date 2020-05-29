# In this program the factorial of a number is calculated

n = int(input('Enter any number: '))  # To read a number

fact = 1

i = 1

while(i <= n):
  fact = fact * i
  i += 1
 
print('The factorial of',n,'is',fact)
