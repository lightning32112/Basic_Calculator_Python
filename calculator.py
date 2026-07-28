#Adding a loop so that if the user wants to they can use the calculator again.
while True:
    try:
        #Asks the user for the function and the numbers they want to put in.
        function = input("Enter operator (+, -, *, /): ")
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        #Sees if the sign is plus then if it is, adds the 2 numbers together.
        if function == "+":
            print("Result:", num1 + num2)
        #Sees if the sign is minus then if it is, subtracts the 2 numbers.
        elif function == "-":
            print("Result:", num1 - num2)
        #Sees if the sign is multiply then if it is, multiplies the 2 numbers together.
        elif function == "*":
            print("Result:", num1 * num2)
        #Checks if the second number is 2, if it is then prints an error otherwise it sees if the sign is division then if it is, divides the 2 numbers.
        elif function == "/":
            if num2 == 0:
                print("Error: Cannot divide by zero.")
            else:
                print("Result:", num1 / num2)
        else:
            print("Error: Invalid operator.")

        #Asks to see if the user wants to use the calculator again.
        run_again = input("Do another? (yes/no): ").strip().lower()
        if run_again != "yes":
            print("Goodbye!")
            break
    except ValueError:
        print("Error: Please enter valid numbers.")

        
