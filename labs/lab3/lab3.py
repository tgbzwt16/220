def traffic():
    road = eval(input("How many roads were surveyed? "))
    total = 0
    for i in range(1, road+1):
        days = eval(input('How many days were road' + " " + str(i) + " " + 'surveyed? '))
        num = 0
        for j in range(1, days+1, 1):
            trav = eval(input('\t' + 'How many cars traveled on day' + " " + str(j) + '? '))
            num = num + trav
            total += trav
            k = num / days
        print('Road', i, 'average vehicles per day:', k)
    print('Total number of vehicles traveled on all roads:', total)
    print('Average number of vehicles per road:', round((total/road), 2))
