"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
"""Psuedocode from lab exercise"""
# repeat forever:
#while loop?
#     read input
#question for user
#     tokenize input
#string split
#         if...
#               elif...
#             (decide which math function to call based on first token)
#             if the first token is 'pow':
#                   call the power function with the other two tokens
#calculation steps 
#         else:
#the first token is "q":
#             quit
#break the loop here

while True:
    math_operations = input("What operations do you wish to use? ")

#    operations_list = 'q add subtract multiply divid square cube pow mod'
    operations_token = math_operations.split(" ")
#lines 35 and 36 converts the items at position 1 and position 2 into intgers
    operations_token[1] = int(operations_token[1])
    operations_token[2] = int(operations_token[2])


    if operations_token[0] == "pow":
        print(power(operations_token[1], operations_token[2]))

    elif operations_token[0] == "+":
      print(add(operations_token[1], operations_token[2]))
    
    elif operations_token[0] == "-":
       print(subtract(operations_token[1], operations_token[2]))

    elif operations_token[0] == "*":
       print(multiply(operations_token[1], operations_token[2]))

    elif operations_token[0] == "/":
       print(divide(operations_token[1], operations_token[2]))

    elif operations_token[0] == "cube":
       print(cube(operations_token[1]))
    
    elif operations_token[0] == "square":
       print(square(operations_token[1]))
    
    elif operations_token[0] == "mod":
       print(mod(operations_token[1], operations_token[2]))
 
    else:
       break
      
