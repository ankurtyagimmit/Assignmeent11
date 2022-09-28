#2. Write a python script to calculate sum of squares of first N natural numbers
N=int(input("Enter n natural number:"))
sum=0

for i in range(1,N+1):
    sum+=(i**2)
    m=i**2
    print(sum,"       ",m)

