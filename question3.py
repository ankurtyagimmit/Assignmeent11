#3. Write a python script to calculate sum of cubes of first N natural numbers
N=int(input("Enter any nutral number"))
sum=0
for i in range(1,N+1):
    sum+=(i**3)
    print(sum,"  ",i**3)

''' N=int(input("Enter n natural number:"))
sum=0

for i in range(1,N+1):
    sum+=(i**2)
    m=i**2
    print(sum,"       ",m)'''


    
