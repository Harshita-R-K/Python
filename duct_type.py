class Employee:
    def __init__(self,first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'
    
    def fullname(self):
        return f'{self.first} {self.last}'

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp1 = Employee('Harshita', 'Kedari', 50000)
emp2 = Employee('Anu', 'shree', 60000)

print(str(emp1))
print(emp1 + emp2)
print(len(emp1))