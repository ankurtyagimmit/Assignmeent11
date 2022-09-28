#4. Write a python script to calculate sum of first N odd natural numbers
N=int(input("Enter any Natural number:"))
sum=0
for i in range(1,N+1):
    if ((i%2!=0)):
        print(i)
        sum=sum+i
print("Total of N odd number is",sum)    
    
