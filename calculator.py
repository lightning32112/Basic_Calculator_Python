#adding a loop so that if the user wants to they can use the calculator again.
while True:
     #Making the variables to see which function/operator the user wants then what numbers the user wants to use.
     function = input("please enter one of the following: +, -, * or /")
     num1 = float(input("choose your first number: "))
     num2 = float(input("choose your second number: "))
   
     print (function)
     print (num1)
     print (num2)
  
     if function == ("+"):
         print ("Your answer is: ", num1 + num2)
     elif function == ("-"):
         print ("Your answer is: ", num1 - num2)
     elif function == ("*"):
         print ("Your answer is: ", num1 * num2)
     elif function == ("/"):
         print ("Your answer is: ", num1 / num2)
