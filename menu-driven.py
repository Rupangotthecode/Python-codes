#menu driven program
print('enter two numbers: ')
a=int(input())
b=int(input())
print('Select Operator: +, -, *, /')
oper=input()
match oper:
    case "+":
        print(a+b)
    case "-":
        print(a-b)
    case "*":
        print(a*b)
    case "/":
        print(a/b)