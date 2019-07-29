class Employee:
    def __init__(self, id, name, salary, salary_raise):
        self.id = id
        self.name = name
        self.salary = salary
        self.salary_raise = salary_raise

    def info(self):
        print("Id:", self.id)
        print("Name:", self.name)
        print("Salary:", self.salary)

    def hire(self):
        print("You are not allowed to use this feature!")

    def increment_salary(self):
        self.salary = self.salary + self.salary * self.salary_raise

    
class Developer(Employee):

    def __init__(self, id, name, salary, salary_raise, desk_id):
        Employee.__init__(self, id, name, salary, salary_raise)
        self.desk_id = desk_id

    def info(self):
        Employee.info(self)
        print("Desk Id:", self.desk_id)


class Manager(Employee):

    def __init__(self, id, name, salary, salary_raise, cabin_id):
        Employee.__init__(self, id, name, salary, salary_raise)
        self.cabin_id = cabin_id

    def info(self):
        Employee.info(self)
        print("Cabin Id:", self.cabin_id)

    def hire(self):
        print("Hiring new resource...")


class Company:

    def __init__(self, employees):
        self.employees = employees

    def employee_list(self):
        for emp in self.employees:
            emp.info()

    def increment_salary(self):
        for emp in self.employees:
            emp.increment_salary()




d1 = Developer(101, "ABC", 10000, 0.3, 1)
# d1.info()
# d1.hire()

m1 = Manager(102, "XYZ", 20000, 0.5, 2)
# m1.info()
# m1.hire()


c = Company([d1, m1])
c.employee_list()
c.increment_salary()
c.employee_list()
