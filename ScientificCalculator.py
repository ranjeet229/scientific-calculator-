import math

str1 = """
    Choose an Operation to proceed: 
    1 or +: Addition         2 or -: Substraction    3 or %: Modulas
    4 or *: Multiplication   5 or /: Division        6 or exp: Exponent
    7 or sqrt: Squareroot    8 or t: Trigonometry    9 or q: Quit
    -> """

str2 = """
    Supported Operations: sin, cos, tan, cot, cosec, sec
    Format: sin(angle), cos(angle), tan(angle),radians,degrees
    Note:- Angle to be input in Radians
    -> """

def operation():
    op = input(str1)
    return op


def process(equation):
    if equation[:3] == 'sin': equation = equation.replace('sin', 'math.sin')
    elif equation[:3] == 'cos': equation = equation.replace('cos', 'math.cos')
    elif equation[:3] == 'tan': equation = equation.replace('tan', 'math.tan')
    elif equation[:3] == 'rad': equation =equation.replace('rad', 'math.radians')
    elif equation[:3] == 'deg': equation =equation.replace('deg','math.degrees')
    return equation
#    if equation[:3] == 'sin': equation.replace('sin', math.sin)


#Supported Operations
lis = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '+']

op = operation()

while True:
    if op=='1' or op=='+':
        print(eval(input('Number 1: ')+'+'+input('Number 2: ')))
        op = operation()
    elif op=='2' or op=='-':
        print(eval(input('Number 1: ')+'-'+input('Number 2: ')))
        op = operation()
    elif op=='3' or op=='%':
        print(eval(input('Number 1: ')+'%'+input('Number 2: ')))
        op = operation()
    elif op=='4' or op=='*':
        print(eval(input('Number 1: ')+'*'+input('Number 2: ')))
        op = operation()
    elif op=='5' or op=='/':
        print(eval(input('Dividend: ')+'/'+input('Divisor: ')))
        op = operation()
    elif op=='6' or op=='exp':
        print(eval(input('Number : ')+'**'+input('Exponent: ')))
        op = operation()
    elif op == '7' or op=='sqrt':
        print(eval(input('Number : ') + '**0.5'))
        op = operation()
    elif op == '8' or op=='t':
        print(eval(process(input(str2))))
        op = operation()
    elif op == 'q' or op=='Q' or op=='9': quit()
    else:
        print("Choose Correct Option, open your Eyes see properly!")
        op = operation()
