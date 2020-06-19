# This program shows how to find maximum of three numbers.

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))

if(a >= b and a >= c):
    print(a,' is largest')
elif(b >= c):
    print(b,' is largest')
else:
    print(c,' is largest')
