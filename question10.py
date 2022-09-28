#10. Write a python script to print the octal equivalent of a given decimal number. (do not use oct() method)
N=int(input("Enter any number: "))
octal=0
ctr=0
Temp=N
while (Temp>0):
    octal+=((Temp%8)*(10**ctr))
    Temp=int(Temp/8)
    ctr +=1
print("Octal of {x} is: {y}".format(x=N,y=octal))    
    
