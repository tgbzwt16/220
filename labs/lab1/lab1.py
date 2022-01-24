# Lab 1 work by Thomas Thornley, 1/24/22

def interest():
    int_rate = eval(input("Please enter the interest rate: "))
    cycle_days = eval(input("Please enter the number of days in the billing cycle: "))
    balance = eval(input("Please enter the net balance: "))
    pay_amount = eval(input("Please enter the payment amount: "))
    pay_date = eval(input("Please enter the day of the billing cycle in which the payment was made: "))
    val1 = balance * cycle_days
    val2 = pay_amount * (cycle_days - pay_date)
    val3 = val1 - val2
    avg_daily_bal = val3 / cycle_days
    monthly_rate = (int_rate / 12)*0.01
    total_charge = monthly_rate * avg_daily_bal
    print("The monthly interest charge is: " + "$", round(total_charge, 2))
