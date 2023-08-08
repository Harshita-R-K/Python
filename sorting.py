class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def __repr__(self):
        return f'({self.name}, {self.age}, ${self.salary})'


e1 = Employee('Carl',25, 70000)
e2 = Employee('Sarah',25, 80000)
e3 = Employee('John',25, 50000)

employees = [e1,e2,e3]

def e_sort(emp):
    return emp.name

print(sorted(employees, key = e_sort))

