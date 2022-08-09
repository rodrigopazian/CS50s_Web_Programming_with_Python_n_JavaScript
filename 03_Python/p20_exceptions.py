#Import sys library to exit from the program before the traceback happens
import sys

#Try to get int values
try:
    x = int(input("x: "))
    y = int(input("y: "))
    #If the exception with error ValueError happens print a message and exit from the system before the traceback
except ValueError:
    print("Error: Invalid Input.")
    #Exit from the program before the traceback sending back value error 1
    sys.exit(1) 

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    sys.exit(1)  

print(f"{x} / {y} = {result}")