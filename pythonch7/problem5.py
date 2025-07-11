#Write a program to find the sum of first n natural numbers using while loop.

n= int(input("enter your number :"))

i=0
sum=0 #initialise sum as 0
while (i<n+1):
    sum=sum+i
    i+=1
print("result is ",sum)
    
i=1
sum=0 #initialise sum as 0
while (i<=n):
    sum=sum+i
    i+=1
    print(sum)
