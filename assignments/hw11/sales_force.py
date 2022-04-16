# Couldn't figure out how to fix the add_data but
# rest of the functions works and produces correct outcomes.
# test in the main at the bottom of codes.

class SalesForce:
    def __init__(self):
        self.sales_people = []

    def add_data(self, filename):

        file = open(filename, 'r')
        for line in file.readlines():
            line = line.rstrip()
            self.sales_people.append(line)

    def quota_report(self, quota):
        result = []
        total = 0
        for i in self.sales_people:
            names = ''.join(i.split(',')[1:2])
            sid = i.replace(',', '')[:3]
            sid = int(sid)
            numbers = ''.join(i.split(',')[2:])
            num = [numbers.split()]
            y = [sid]
            for nums in num:
                total = 0
                for x in nums:
                    x = float(x)
                    total += x
                y.append(names)
                y.append(total)
            result.append(y)
            if total >= quota:
                y.append(True)
            if total < quota:
                y.append(False)
        return result

    def top_seller(self):
        nums = []
        for i in self.sales_people:
            numbers = ''.join(i.split(',')[2:])
            num = [numbers.split()]
            for x in num:
                for j in x:
                    j = float(j)
                    nums.append(j)

        biggest = max(nums)
        top = []
        result = []
        for i in self.sales_people:
            names = ''.join(i.split(',')[1:2])
            sid = i.replace(',', '')[:3]
            sid = int(sid)
            numbers = ''.join(i.split(',')[2:])
            num = [numbers.split()]
            y = [sid]
            for nums in num:
                y.append(names)
                for x in nums:
                    x = float(x)
                    y.append(x)
            result.append(y)

        for info in result:
            if biggest in info:
                top.append(info[1])
        return top

    def individual_sales(self, employee_id):
        result = []
        for i in self.sales_people:
            names = ''.join(i.split(',')[1:2])
            sid = i.replace(',', '')[:3]
            sid = int(sid)
            numbers = ''.join(i.split(',')[2:])
            num = [numbers.split()]
            y = [sid]
            for nums in num:
                for x in nums:
                    x = float(x)
                y.append(names)
            result.append(y)

        for line in result:
            if employee_id in line:
                return line[1]
            return None

    def get_sale_frequencies(self):
        freq = {}
        nums = []
        for i in self.sales_people:
            numbers = ''.join(i.split(',')[2:])
            num = [numbers.split()]
            for x in num:
                for j in x:
                    j = float(j)
                    nums.append(j)

        for item in nums:
            if item in freq:
                freq[item] += 1
            else:
                freq[item] = 1
        return freq


# Can't see my functions test results so I made this.
if __name__ == '__main__':
    s = SalesForce()
    s.add_data('sales_data.txt')
    print(s.sales_people)
    print(s.quota_report(1200))
    print(s.top_seller())
    print(s.individual_sales(123))
    print(s.get_sale_frequencies())
