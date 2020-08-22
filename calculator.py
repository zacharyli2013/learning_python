import math
import time
import sys
import os

def pr_reset(ty):
    if ty == "not found":
        print("operator not found. reseting...")
        time.sleep(3)
    elif ty == "found":
        print("reseting...")
        time.sleep(3)

def pr_exit():
    while True:
        exiting = input("exit? (enter 'true' or 'false') ")
        if exiting == "true":
            print("exiting...")
            time.sleep(3)
            break
        elif exiting == "false":
            print("not exiting")
        else:
            print("you did not enter 'true' or 'false'.")
    os._exit(0)

def pr_add(num1, num2):
    print(num1 + num2)

def pr_subtract(num1, num2):
    print(num1 - num2)

def pr_multiply(num1, num2):
    print(num1 * num2)

def pr_divide(num1, num2):
    print(num1 / num2)

def pr_mod(num1, num2):
    print(num1 % num2)

def pr_cos(num):
    print(math.cos(num))

def pr_sin(num):
    print(math.sin(num))

def pr_sqrt(num):
    print(math.sqrt(num))

def pr_tan(num):
    print(math.tan(num))

def pr_atan(num):
    print(math.atan(num))

def pr_acos(num):
    print(math.acos(num))

def pr_asin(num):
    print(math.asin(num))

def pr_floor(num):
    print(math.floor(num))

def pr_ceil(num):
    print(math.ceil(num))

while True:
    operator = input("choose operater ")
    print("if your doing sin and cos and that stuff,\nyou can just type '0'\nwhen the computer asks you'input second number'.")
    num1 = float(input("Input your first number: "))
    num2 = float(input("Input your second number: "))
    if operator == "add" or operator == "+":
        pr_add(num1, num2)
        pr_exit()
    elif operator == "subtract" or operator == "-":
        pr_subtract(num1, num2)
        pr_exit()
    elif operator == "multiply" or operator == "*":
        pr_multiply(num1, num2)
        pr_exit()
    elif operator == "divide" or operator == "/":
        pr_divide(num1, num2)
        pr_exit()
    elif operator == "mod" or "%":
        pr_mod(num1, num2)
        pr_exit()
    elif operator == "cos":
        pr_cos(num1)
        pr_exit()
    elif operator == "sin":
        pr_sin(num1)
        pr_exit()
    elif operator == "sqrt":
        pr_sqrt(num1)
        pr_exit()
    elif operator == "tan":
        pr_tan(num1)
        pr_exit()
    elif operator == "acos":
        pr_acos(num1)
        pr_exit()
    elif operator == "asin":
        pr_asin(num)
        pr_exit()
    else:
        pr_reset("not found")
        pr_exit()