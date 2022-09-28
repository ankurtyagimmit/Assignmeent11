#8. Write a python script to calculate sum of digits of a given number
Number=int(input("Enter any digit:"))
count=0
sum=0
while(Number!=0):
    Number//=10
    count+=1
    
    print(str(count))
    sum+=count
print("Sum of %d digit is %d"%(count,sum))
    
    
