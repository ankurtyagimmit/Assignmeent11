#5. Write a python script to calculate sum of first N even natural numbers
N=int(input("Enter Natural Number:"))
sum=0
for e in range(1,N+1):
    if ((e%2)==0):
        print(e)
        sum=sum+e
        
print("Total of N even number is:",sum)
