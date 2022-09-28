#7. Write a python script to count digits in a given number
N=int(input("Enter any number:"))
count=0
while(N!=0):
    N//=10
    count+=1
print("Digits of given number Is:", str(count))
    
