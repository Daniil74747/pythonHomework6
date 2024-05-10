class Calculator:
    num1: str
    num2: str
    a: str

    def __init__(self, num1, num2, a):
        self.num1 = num1
        self.num2 = num2
        self.a = a

num1 = input(str('Enter a first number: '))
num2 = input(str('Enter a second number: '))
a = input(str('Choose an action(+,-,*,/): '))

try:
    num1 = float(num1)
    num2 = float(num2)
except (TypeError, ValueError) as error:
    print(-1, error)

try:
    if a == '+':
        print(num1 + num2)
    elif a == '-':
        print(num1 - num2)
    elif a == '*':
        print(num1 * num2)
except TypeError as error:
    print(-1, error)
if a == '/':
    try:
        print(num1 / num2)
    except (ZeroDivisionError, TypeError) as error:
        print(-1, error)
    finally:
        print('Error')