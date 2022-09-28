#1. Write a python script to calculate sum of first N natural numbers
N=int(input("Enter N natural Number:"))
sum=0
for i in range(1,N+1):
    sum=sum+i
    print(i,"    ",sum)
