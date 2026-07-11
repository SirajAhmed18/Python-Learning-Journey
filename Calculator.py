# Building a Simple Calculator with user choice Operations

a = float(input("Enter 1st number: "))   
b = float(input("Enter 2nd number: "))
c= input("choose your operation (+ , - , * , ** , /): ")

if c == "+":
    print("The Addition of Two Numbers is:",a+b)
elif c == "-":
    print ("The Subtraction of Two Numbers is:", a-b)
elif c == "*":
    print ("The Multiplication of Two Numbers is:", a*b)
elif c == "/":
    if b == 0:
        print ("Division by Zero is Undefined")
    else:
        print("The Division of Two Numbers is:", a/b)
elif c == "**":
    print(f"{a} raised to the power {b} is: ", a**b)
else:
    print("Operation not found")