def calculator():
    
    num1 = float(input("Enter the first number: ")) #asking the user to enter the first number
    
    num2 = float(input("Enter the second number: "))#asking the user to enter the second number
    
    print("select the operation you need to perform:")#asking for the operation that needs to be performed
    print(" a. Addition (+)")
    print(" b. Subtraction (-)")
    print(" c. Multiplication (*)")
    print(" d. Division (/)")
    operation = input("Enter the operation (a/b/c/d): ")
    
    #performing calculations based on the selection made by the user
    if operation == 'a': or operation == '+':
        result = num1 + num2
        operator= '+'
    elif operation == 'b' or operation == '-':
        result = num1 - num2
        operator = '-'
    elif operation == 'c' or operation == '*':
        result = num1 * num2
        operator = '*'
    elif operation == 'd' or operation == '/':
        if num2 != 0:
            result = num1 / num2
            operator = '/'
        else:
            result = "undefined (division by zero)"
            operator = '/'
    else:
        result = "invalid operation"
        opeartor = ''
    
    if isinstance(result, float):
        print(f"The result of {num1} {operator} {num2} is: {result}")
    else:
        print(result)

#invoking the function
calculator()
