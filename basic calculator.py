def calculator():
    # Ask the user to enter the first number
    number1 = float(input("Enter the first number :"))

    # Ask the user to enter the second number
    number2 = float(input("Enter the second number:"))

    # Ask the user to enter an operation
    print(" Scelect an operation:")
    print(" A. Addition(+)")
    print(" B. Substraction(-)")
    print(" C. Multiplication(*)")
    print(" D. Division(/)")

    operation = input("Enter your choice(A/B/C/D):")

    #performing calculations based on the user's choice

    if operation =='A':
         result = number1 + number2
         
         print(f"The result of the operation is : {result}")

    elif operation =='B':
         result = number1 - number2
         print(f"The result of the operation is : {result}")

    elif operation =='C':
         result = number1 * number2
         print(f"The result of the operation is : {result}")

    elif operation =='D':
        if number2 != 0:
            result = number1 / number2
            print(f"The result of the operation is : {result}")
        else:
            print("ERROR : Divition by ZERO is NOT ALLOWED.")
    else:
        print("INVALID OPERATION CHOICE. PLEASE SELECT BETWEEN A, B, C, OR D.")

calculator()
            
        
          
          
