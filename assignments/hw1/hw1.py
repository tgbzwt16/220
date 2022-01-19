"""
Name: Thomas Thornley
<ProgramName>.py

Problem: Creating functions with inputs to allow users to perform different computations.

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("volume =", volume)


def shooting_percentage():
    shots_taken = eval(input("Enter the amount taken: "))
    shots_made = eval(input("Enter the amount made: "))
    shooting_per = (shots_made/shots_taken)*100
    print("shooting percentage =", shooting_per)


def coffee():
    amount = eval(input("How much pounds of coffee would you like? "))
    cof_per_lb = 10.5
    ship_cost = 0.86
    overhead_cost = 1.5
    total_cost = amount*(cof_per_lb+ship_cost)+overhead_cost
    print("total cost =", round(total_cost, 2))


def kilometers_to_miles():
    amount = eval(input("How many kilometers did you travel? "))
    kl_to_mi = 1.61
    total = amount / kl_to_mi
    print("total miles =", total)
