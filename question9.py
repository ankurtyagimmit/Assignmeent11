"""9. Write a python script to print binary equivalent of a given decimal number. (do not
use bin() method)"""
N=int(input("Enter any number:"))
binary=0
Mul=1
while(N>0):
    Rem=N%2
    binary=binary+(Rem*Mul)
    Mul=Mul*10
    N=int(N/2)
print("Binary is:",binary)

    
