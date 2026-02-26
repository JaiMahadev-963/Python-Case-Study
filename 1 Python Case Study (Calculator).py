import math
def fact(x):
    fact = 1
    for i in range(1, x+1):
        fact*=i
    return fact
print("Jai Mahadev....!")
print("Calculator is Ready!")
print()
a = int(input("Enter 1st Number: "))
b = int(input("Enter 2nd Number: "))


print("Addition--> 1\nSubtraction--> 2\nMultiplication--> 3\nDivision--> 4\nPower--> 5\nModulus--> 6\nFactorial-->7\nSquar Root--> 8\nExit--> 9")
print()
x = int(input("Press operations related key: "))

if(x==1):
    print(a+b)
elif(x==2):
    print(a-b)
elif(x==3):
    print(a*b)
elif(x==4):
    print(a/b)
elif(x==5):
    print(a**b)
elif(x==6):
    print(a%b)
elif(x==7):
    print("Factorial of 1st number: ",fact(a))
    print("Factorial of 2nd number: ",fact(b))
elif(x==8):
    print("Square root of 1st number: ",math.sqrt(a))
    print("Square root of 2nd number: ",math.sqrt(b))
elif(x==9):
    exit()
else:
    print("Wrong input!")
