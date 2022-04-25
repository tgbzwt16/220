def read_data(filename):
    nums = []
    file = open(filename, 'r')
    lines = list(file.readlines())
    k = 0
    while k < len(lines):
        line = lines[k].rstrip()
        result = line.split()
        nums.append(result)
        k += 1
    final = sum(nums, [])

    data = []
    i = 0
    while i < len(final):
        x = int(final[i])
        data.append(x)
        i += 1
    return data


def is_in_linear(search_val, values):
    i = 0
    while i < len(values):
        if search_val in values:
            return True
        return False


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


if __name__ == '__main__':
    print(read_data('data_sorted.txt'))
    print(is_in_linear(53, read_data('data_sorted.txt')))
    print(is_in_linear(52, read_data('data_sorted.txt')))
