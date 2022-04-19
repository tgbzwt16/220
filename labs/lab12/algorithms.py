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


if __name__ == '__main__':
    print(read_data('data_sorted.txt'))
    print(is_in_linear(53, read_data('data_sorted.txt')))
    print(is_in_linear(52, read_data('data_sorted.txt')))
