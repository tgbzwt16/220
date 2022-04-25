from graphics import *


def is_in_binary(search_val, values):
    low = 0
    high = len(values) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        if values[mid] < search_val:
            low = mid + 1
        elif values[mid] > search_val:
            high = mid - 1
        else:
            return True
    return False


def selection_sort(values):
    for i in range(len(values)):
        low = i
        for j in range(i+1, len(values)):
            if values[low] > values[j]:
                low = j
        values[i], values[low] = values[low], values[i]
    return values


def calc_area(rect):
    x1 = rect.getP1().getX()
    x2 = rect.getP2().getX()

    y1 = rect.getP1().getY()
    y2 = rect.getP2().getY()

    area = (x2 - x1) * (y2 - y1)
    return int(area)


def rect_sort(rectangles):
    for i in range(len(rectangles)):
        low = calc_area(rectangles[i])
        for j in range(i + 1, len(rectangles)):
            k = calc_area(rectangles[j])
            if low > k:
                low = j
        rectangles[i], rectangles[i] = rectangles[i], rectangles[i]
    return rectangles


def trade_alert(filename):
    file = open(filename, 'r')
    line = file.readline()
    line = line.rstrip()
    line1 = ''.join(line.split(',')[0:])
    num = line1.split()
    for i in range(len(num)):
        k = int(num[i])
        if k > 830:
            print('volume exceeded 830 at' + ' ' + str(i + 1) + ' ' + 'seconds')
        elif k == 500:
            print('volume is equal to 500 at' + ' ' + str(i + 1) + ' ' + 'seconds')


if __name__ == '__main__':
    x = [400, 1, 202, 12, 44, 6]
    print(selection_sort(x))
    x = [40, -1, 22, 2, 4, 6]
    print(selection_sort(x))
    rectangle = [Rectangle(Point(6, 17), Point(33, 55)),  Rectangle(Point(12, 34), Point(20, 50)),
                 Rectangle(Point(5, 23), Point(20, 56)), Rectangle(Point(9, 17), Point(33, 55))]
    print(rect_sort(rectangle))
    print(trade_alert('trades.txt'))
