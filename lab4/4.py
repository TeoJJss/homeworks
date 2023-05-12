def add(num1, num2):
    return num1+num2

def substract(num1, num2):
    return num2-num1

def multiply(num1, num2):
    return num1*num2

def divide(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        return "ERROR: Division with zero"

print("Calculator:\n1. ADD\n2. SUBTRACT\n3. MULTIPLY\n4. DIVIDE")

option=int(input("Choose the operation from the given options: "))
if option in range(1,5):
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))
    result=o=""

    match(option):
        case 1:
            o="Sum"
            result=add(num1, num2)
        case 2:
            o="Difference"
            result=substract(num1, num2)
        case 3:
            o="Product"
            result=multiply(num1, num2)
        case 4:
            o="Quotient"
            result=divide(num1, num2)
        case _:
            print("Invalid option! ")
else:
    print("Invalid option! ")
print(f"{o} of {num1} and {num2} is {result}")