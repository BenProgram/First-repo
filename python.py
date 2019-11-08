class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@injection.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('kasongo', 'Freddy', 6000)
emp_2 = Employee('benjamin', 'malunda', 50000)

print(emp_1.fullname())