#Task 1: Calculate Factorial Using a Function

def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=num
        num-=1
    return fact

num=int(input("Enter a number: "))
result=factorial(num)
print(f"Factorial of {num} is: {result}")