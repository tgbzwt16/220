"""
Name: Thomas Thornley
hw5.py

Problem: Writing programs to manipulate strings, lists.

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""


def name_reverse():
    name = input("enter a name (first last): ")
    list1 = name.split()
    l_name = list1[1]
    f_name = list1[0]
    print(l_name + ', ' + f_name)


def company_name():
    domain = input("enter a domain: ")
    domain = domain.replace('www.', '')
    domain = domain.replace('.com', '')
    print(domain)


def initials():
    amount = eval(input("How many students are in the class? "))

    for i in range(1, amount + 1):
        name = input("what is the name of the student" + " " + str(i) + "? ")
        list1 = name.split()
        f_letter = list1[0][0]
        l_letter = list1[1][0]
        print(f_letter + l_letter)


def names():
    name = input('enter a list of names: ')
    name = name.replace(',', '')
    list1 = name.split()
    for i in range(0, len(list1), 2):
        val1 = list1[i]
        val2 = list1[i+1]
        f_letter = val1[0]
        l_letter = val2[0]
        print(f_letter + l_letter)


def thirds():
    num_sen = eval(input('enter the number of sentences: '))
    sen_str = ''
    for i in range(1, num_sen + 1):
        sen = input('enter sentence ' + str(i) + ': ')
        sen.split(' ')
        sen_str += sen[0][0] + sen[3::3]
    print(sen_str)


def word_average():
    sentence = input('enter a sentence: ')
    new_sen = sentence.split(' ')
    sentence = sentence.replace(' ', '')
    sen_len = len(sentence)
    total = 0
    for i in new_sen:
        total = total + 1

    avg = sen_len / total
    print(avg)


def pig_latin():
    sen = input('enter a sentence to convert to pig latin: ')
    f_letter = []
    sen = sen.lower()
    sen = sen.split()
    for i in sen:
        f_letter += [i[1:] + i[0] + 'ay']

    new_str = ' '.join(f_letter)
    print(new_str)


if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()
    pass
