"""
Name: Thomas Thornley
hw6.py

Problem: creating string/arithmetic functions

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""

import math


def cash_converter():
    amount = eval(input('enter an integer: '))
    print('that is ${:.2f}'.format(amount))


def encode():
    msg = input('enter a message: ')
    key = eval(input('enter a key: '))
    original = []
    cipher_list = []
    encoded = []
    for i in msg:
        original += [ord(i)]
    for i in original:
        cipher = i + key
        cipher_list.append(cipher)
    for i in cipher_list:
        encoded += [chr(i)]

    new_list = ''.join(encoded)
    print(new_list)


def sphere_area(radius: float):
    val = 4 * math.pi
    area = val * (radius ** 2)
    return area


def sphere_volume(radius: float):
    val = (4/3) * math.pi
    volume = val * (radius ** 3)
    return volume


def sum_n(number: int):
    total = 0
    for i in range(number):
        acc = 1 + i
        total += acc
    return total


def sum_n_cubes(number: int):
    total = 0
    for i in range(number):
        acc = (1 + i) ** 3
        total += acc
    return total


def encode_better():
    msg = input('enter a message: ')
    key = input('enter a key: ')
    length = len(msg)

    original = []
    key_list = []
    encoded = []
    final = []

    # getting ord() of the message
    for i in msg:
        original += [abs(ord(i) - 65)]

    # repeating key based on length of the message
    num = length // len(key) + 1
    str1 = key * num
    str2 = str1[:length]

    # getting ord() of the repeated key
    for i in str2:
        key_list += [ord(i)]

    # summing the ord() of the repeated key and message
    for i in range(0, len(original)):
        encoded.append(original[i] + key_list[i])

    # shifting values
    for i in encoded:
        i = i - 58
        final += [chr(abs(i))]

    final = ''.join(final)
    print(final)


if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()
    pass
