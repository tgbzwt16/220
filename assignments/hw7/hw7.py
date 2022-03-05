"""
Name: Thomas Thornley
hw7.py

Problem: Working with string functions.

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""
from encryption import encode, encode_better


def number_words(in_file_name, out_file_name):
    file_open = open(in_file_name, 'r')
    file_out = open(out_file_name, 'w')
    k = 1
    for i in file_open.read().split():
        val = str(k) + ' ' + i + '\n'
        file_out.write(val)
        k += 1


def hourly_wages(in_file_name, out_file_name):
    file_open = open(in_file_name, 'r')
    file_out = open(out_file_name, 'w')
    file_list = []
    bonus = 1.65

    for line in file_open.read().split():
        file_list += [line]
        val1 = file_list[2::4]

    for i in range(len(val1)):
        pay = (float(file_list[2::4][i]) + bonus) * (float(file_list[3::4][i]))
        names = file_list[0::4][i] + ' ' + file_list[1::4][i]
        pay_format = "{0:.3f}".format(pay)
        final = names + ' ' + str(pay_format[:-1]) + '\n'
        file_out.write(final)


def calc_check_sum(isbn):
    isbn = isbn.replace('-', '')
    k = 10
    total = 0
    for j in isbn:
        num = (int(j) % 11)
        num = num * k
        total += num
        k -= 1
    return total


def send_message(file_name, friend_name):
    file_open = open(file_name, 'r')
    name_file = friend_name + '.txt'
    new_file = open(name_file, 'w')
    for line in file_open:
        new_file.write(line)


def send_safe_message(file_name, friend_name, key):
    file_open = open(file_name, 'r')
    name_file = friend_name + '.txt'
    new_file = open(name_file, 'w')
    for line in file_open.readlines():
        line = encode(line.strip(), key)
        new_file.write(line)
        new_file.write('\n')


def send_uncrackable_message(file_name, friend_name, pad_file_name):
    file_open = open(file_name, 'r')
    pad = open(pad_file_name, 'r')
    name_file = friend_name + '.txt'
    new_file = open(name_file, 'w')

    key = pad.read().strip()
    msg = file_open.read()
    encoded = encode_better(msg, key)
    new_file.write(encoded)


if __name__ == '__main__':
    pass
