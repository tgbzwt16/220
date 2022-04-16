class SalesPerson:
    def __init__(self, sid, name):
        self.sid = sid
        self.name = name
        self.sales = []

    def get_id(self):
        return self.sid

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(sale)

    def total_sales(self):
        total = float(sum(self.sales))
        return total

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        if float(sum(self.sales)) == quota:
            return True
        return False

    def compare_to(self, other):
        if float(sum(self.sales)) > other:
            return 1
        elif float(sum(self.sales)) < other:
            return -1
        elif float(sum(self.sales)) == other:
            return 0

    def __str__(self):
        result = str(self.sid) + '-' + self.name + ':' + str(float(sum(self.sales)))
        return result


if __name__ == '__main__':
    s = SalesPerson(1, 'luke')
    print(s.set_name('mark'))
    print(s.get_id())
    print(s.get_name())
    print(s.enter_sale(12.45))
    print(s.enter_sale(13.45))
    print(s.enter_sale(15.45))
    print(s.enter_sale(16.45))
    print(s.get_sales())
    print(s.total_sales())
    print(s.met_quota(57.8))
    print(s.compare_to(112))
    print(s.__str__())

