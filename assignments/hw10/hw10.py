"""
Name: Thomas Thornley
<ProgramName>.py

Problem: Creating while loop functions.

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""
import math


def fibonacci(num):
    count = 2
    val1 = 0
    val2 = 1
    val = 0
    if num in (1, 2):
        return 1
    if num < 1:
        return None

    while count <= num:
        val = val1 + val2
        val1 = val2
        val2 = val
        count += 1
    return val


def double_investment(principle, rate):
    count = 0
    target = 2 * principle

    while principle < target:
        num = principle * (1 + rate)
        count += 1
        principle = num
    return count


def syracuse(num):
    list1 = [num]
    while num != 1:
        if num % 2 == 1:
            k = (num * 3) + 1
            list1.append(k)
            num = k
        elif num % 2 == 0:
            k = num / 2
            list1.append(k)
            num = k
    return list1


def isprime(num):
    val = 2
    while val <= math.sqrt(num):
        if num % val < 1:
            return False
        val += 1
    return num > 1


def goldbach(num):
    if num % 2 == 1:
        return None
    target = num
    prime = []
    result = []
    i = 0
    complementary = 0
    number = 0

    while num != 1:
        num -= 1
        if isprime(num) is True:
            prime.append(num)
            number = num
            complementary = target - number
        if complementary in prime[i:]:
            result.append(number)
            result.append(complementary)
            i += 1
            return result
