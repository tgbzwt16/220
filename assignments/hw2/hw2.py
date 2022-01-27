"""
Name: Thomas Thornley
hw2.py

Problem: Writing functions to solve arithmetic problem.

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""
import math


def sum_of_threes():
    upper_bound = eval(input("Enter the value of the upper bound: "))
    num_list = []
    for i in range(upper_bound+1):
        if i % 3 == 0:
            num_list.append(i)
            j = sum(num_list)
    print(j)


def multiplication_table():
    for i in range(1, 11):
        for j in range(1, 11):
            print(i * j, end="\t")
        print()


def triangle_area():
    a_side = eval(input("Enter the length of the side: "))
    b_side = eval(input("Enter the length of the side: "))
    c_side = eval(input("Enter the length of the side: "))
    val1 = a_side+b_side+c_side
    sval = val1/2
    pre_area = (sval-a_side)*(sval-b_side)*(sval-c_side)*sval
    print(math.sqrt(pre_area))


def sum_squares():
    lower_val = eval(input("Enter the value of the lower range: "))
    upper_val = eval(input("Enter the value of the upper range: "))
    new_list = []
    final_list = []
    for i in range(lower_val, upper_val + 1):
        new_list.append(i)
    for i in new_list:
        final_list.append(i ** 2)
        total = sum(final_list)
    print(total)


def power():
    base = eval(input("Enter the value of the base: "))
    exponent = eval(input("Enter the value of the exponent: "))
    pwr = exponent
    result = 1
    while pwr > 0:
        result = result * base
        pwr -= 1
    print("{} ^ {} = ".format(base, exponent), result)
