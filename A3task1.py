a=int(input("enter a number:"))
def factorial(a):
    if a<2:
        return 1
    else:
        return a*factorial(a-1)
print("the factorial of",a,"is:",factorial(a))
