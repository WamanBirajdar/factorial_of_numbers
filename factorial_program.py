# written program with three method first math module, recursion and iterative method

#using inbuild function

import math

number = int(input("Enter the numbber"))
result = math.factorial(number)
print("Here is your factorial of given number",result)



#factorial of number using recursion
n = int(input("Entee the number"))

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

result=fact(n)
print("Factorial of ",n,"is",result)


#find out factorial with iterating

n=int(input("Enter the number"))
output=1
for i in range(1,0,-1):
    ouput=i*output
    print(output)
