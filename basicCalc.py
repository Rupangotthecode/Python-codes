num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
op=input("what operation do you want?")
match op:
    case "+":
        print(num1+num2)
    case "-":
        print(num1-num2)
    case "/":
        print(num1/num2)
    case "*":
        print(num1*num2)
    case "%":
        print(num1%num2)