def weighted_average(in_file_name, out_file_name):

    file_open = open(in_file_name, 'r')
    file_out = open(out_file_name, 'w')
    class_avg = 0
    check = 0
    total = 0
    for line in file_open.readlines():
        weighted_val = 0
        line = line.strip()
        line = line.split(': ')
        num_list = line[1].split(' ')
        for i in range(0, len(num_list), 2):
            total += int(num_list[i]) * int(num_list[i + 1])
            weighted_val = weighted_val + int(num_list[i])
            if weighted_val == 100:
                val = total / 100
                class_avg += val
                check += 1
            if weighted_val < 100:
                print('Error, the weight is less than 100', file=file_out)
            else:
                print('Error, the weight is more than 100', file=file_out)
    print('class average: ', class_avg / check, file=file_out)

    if __name__ == '__main__':
        weighted_average(grades.txt, avg.txt)
