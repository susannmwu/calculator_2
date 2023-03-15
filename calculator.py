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
#         if the first token is "q":
#             quit
#break the loop here
#calculation steps 
#         else:
#             (decide which math function to call based on first token)
#             if the first token is 'pow':
#                   call the power function with the other two tokens

#             (...etc.)

while True:
   math_operations = input("What operations do you wish to use? ")
   
   tokens = math_operations.split(" ")

   
