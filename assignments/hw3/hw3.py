"""
Name: Thomas Thornley
hw3.py

Problem: Using loops to write functions.

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""


def average():
    question = eval(input("How many grades will you enter? "))
    sum_ = 0
    for i in range(question):
        grade = eval(input("Enter grade: "))
        sum_ = sum_ + grade
        total = sum_ / question
        i -= 1
    print(total)


def tip_jar():
    total = 0
    ppl_tipping = 5
    for i in range(ppl_tipping):
        tips = eval(input("How much would you like to donate? "))
        total += tips
        i -= 1
    print(total)


def newton():
    var1 = eval(input("What number do you want to square root? "))
    times = eval(input("How many times should we improve the approximation? "))
    initial = var1
    for i in range(times):
        initial = (initial + var1/initial)/2
        i -= 1
    print(initial)


def sequence():
    terms = eval(input("How many terms would you like? "))
    for i in range(1, terms+1):
        while i % 2 == 0:
            i = i-1
        print(i, end=' ')


def pi():
    series = eval(input("How many terms in the series? "))
    multi = 1
    j = 1
    i = 1
    for i in range(2, series + 2):
        while i % 2 == 0:
            i = i - 1
    for j in range(2, series + 2):
        while j % 2 == 1:
            j = j - 1
    multi = multi * (j / i) * (j / i)
    print(2*multi)
