# Write a program to print the following star pattern. 
#   * 
#  *** 
# *****       for n = 3 

n=int(input("enter your number"))

for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end="")
    print("\n")
   
# pyramid
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1))
    print("\n")
   

#inverted
n = 5
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))


#diamond
n = 3
# Upper half
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
# Lower half
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))

for i in range(n-1,-1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1))
    print("\n")

# right sided
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)


#hollow square pattern
n = 7

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
