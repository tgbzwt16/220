import math


def mean():
    question = eval(input("Enter the values to be entered: "))
    list1 = []
    list2 = []
    list3 = []
    multi = 1
    for i in range(1, question + 1):
        value = eval(input("Enter value: "))
        list1.append(value)
    for i in list1:
        k = i * i
        list2.append(k)
        pre_total = sum(list2)
        total = pre_total / question
        math.sqrt(total)
    print(round((math.sqrt(total)), 3))

    for i in list1:
        j = 1 / i
        list3.append(j)
        num_total = sum(list3)
        harmonic = question / num_total
    print(round(harmonic, 3))

    for i in list1:
        multi = multi * i
        geometric = multi ** (1 / question)
    print(round(geometric, 3))
