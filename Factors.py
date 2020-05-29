# In this program, the factors of a number are printed

n = int(input('Enter any number : ')) # To read a number

for i in range(1,n//2+1):
  if(n % i == 0):
    print(i,end=' ')
print(n)
