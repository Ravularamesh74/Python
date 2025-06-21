op= input("Enter any one option choose (+, -, *, /): ")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if op == "+":
    print("add of two no", a + b)
elif op == "-":
    print("subtract of two no", a - b)
elif op == "*":
    print("multiply of two no", a * b)
elif op == "/":
    if b != 0:
        print("divide of two no", a / b)
    else:
        print("it is not correct.")
else:
    print("Invalid operator.")