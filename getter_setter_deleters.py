class Employee:
    def __init__(self,first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return f'{self.first}.{self.last}@gmail.com'
    
    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self,name):
        self.first,self.last = name.split(' ')

    @fullname.deleter
    def fullname(self):
        print("Full name will be deleted!")
        self.first = None
        self.last = None

emp1 = Employee('Harshita', 'Kedari', 50000)
emp2 = Employee('Anu', 'shree', 60000)

emp1.fullname = 'Divya Shree'

print(emp1.email)
print(emp2.fullname)
print(emp1.fullname)
del emp1.first