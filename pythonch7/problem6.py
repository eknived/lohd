# Write a program to calculate the factorial of a given number using for loop
import math
n= int(input("enter your number"))

print(math.factorial(n))

i=1
fact=1
for i in range(n+1):
    fact=fact*i
    i+=1
print(fact)
