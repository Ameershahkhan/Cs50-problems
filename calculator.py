def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def multiple(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        print("Division by 0 is not allowerd")
        return None
    return a / b


def remainder(a, b):
    if b == 0:
        print("Division by 0 is not allowerd")
        return None
    return a % b


def power(a, b):
    return a ** b


def square_root(a):
    return a ** (1 / 2)


def square(a):
    return a ** 2


print("Enter \"q\" to quit.")
print("Enter \"root\" to find the square root.")
print("Enter \"square\" to find square. ")

num1 = float(input("Enter a number : "))
while True:
    operator = input("Enter operation : ")

    if operator == "root":
        result = square_root(num1)
        print(f"Square root : {result}")
        num1 = result
        continue
    elif operator == "square":
        result = square(num1)
        print(f"Square : {result}")
        num1 = result
        continue
    elif operator == "q":
        print(f"final result ; {result}")
        break

    num2 = float(input("Enter 2nd number : "))

    if operator == "+":
        result = add(num1, num2)
    elif operator == "-":
        result = sub(num1, num2)
    elif operator == "*":
        result = multiple(num1, num2)
    elif operator == "/":
        result = divide(num1, num2)
    elif operator == "**":
        result = power(num1, num2)
    elif operator == "%":
        result = remainder(num1, num2)

    print("result : ", result)

    num1 = result
