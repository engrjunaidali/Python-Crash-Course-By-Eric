def divide(a,b):
    return a/b

def multiply(a,b):
    return a*b

def add(a,b):
    return a + b

def minus(a,b):
    return a - b

YesNo = 1
while YesNo == 1:

    a = 2
    b = 3

    print("1. Divide\n2. Multiply\n3. Add\n4. Minus\n5. Power")
    n = int(input("Enter n: "))
    if n==1:
        print(divide(a,b))
    elif n == 2:
        print(multiply(a,b))
    elif n == 3:
        print(add(a,b))
    elif n == 4:
        print(minus(a,b))

    YesNo = int(input("\nDo you want to try again :\n1. Yes\n2. No\n"))