class Employee:
    def __init__(self, emp_id, name, dept):
        self.emp_id, self.name, self.dept = emp_id, name, dept
    
    def calculate_salary(self):
        pass
    
    def display(self):
        print(f"--- Employee Details ---\nEmployee ID: {self.emp_id}\nName: {self.name}\nDepartment: {self.dept}")

class Permanent(Employee):
    def __init__(self, emp_id, name, dept, salary, bonus):
        super().__init__(emp_id, name, dept)
        self.salary, self.bonus = salary, bonus
    
    def calculate_salary(self): return self.salary + self.bonus
    
    def display(self):
        super().display()
        print(f"Basic Salary: ${self.salary:.2f}\nBonus: ${self.bonus:.2f}\nTotal Salary: ${self.calculate_salary():.2f}\n")

class Contract(Employee):
    def __init__(self, emp_id, name, dept, rate, hours):
        super().__init__(emp_id, name, dept)
        self.rate, self.hours = rate, hours
    
    def calculate_salary(self): return self.rate * self.hours
    
    def display(self):
        super().display()
        print(f"Hourly Rate: ${self.rate:.2f}\nHours Worked: {self.hours}\nTotal Salary: ${self.calculate_salary():.2f}\n")

class Intern(Employee):
    def __init__(self, emp_id, name, dept, stipend):
        super().__init__(emp_id, name, dept)
        self.stipend = stipend
    
    def calculate_salary(self): return self.stipend
    
    def display(self):
        super().display()
        print(f"Stipend: ${self.stipend:.2f}\nTotal Salary: ${self.calculate_salary():.2f}\n")

employees = []
for _ in range(int(input("Number of employees: "))):
    emp_type = input("Type (Permanent/Contract/Intern): ").strip().lower()
    emp_id, name, dept = input("ID: "), input("Name: "), input("Dept: ")
    
    if emp_type == "permanent":
        employees.append(Permanent(emp_id, name, dept, float(input("Salary: ")), float(input("Bonus: "))))
    elif emp_type == "contract":
        employees.append(Contract(emp_id, name, dept, float(input("Rate: ")), int(input("Hours: "))))
    elif emp_type == "intern":
        employees.append(Intern(emp_id, name, dept, float(input("Stipend: "))))
    else:
        print("Invalid type.")

for emp in employees: emp.display()
