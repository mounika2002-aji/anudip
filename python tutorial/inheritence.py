class Department:
    def _init_(self, department_name, head_of_department, number_of_employees):
        self.department_name = department_name
        self.head_of_department = head_of_department
        self.number_of_employees = number_of_employees

    def department_info(self):
        print(f"Department Name: {self.department_name}")
        print(f"Head of Department: {self.head_of_department}")
        print(f"Number of Employees: {self.number_of_employees}")
        
class HR(Department):
    def _init_(self, department_name, head_of_department, number_of_employees, recruitment_status):
        super()._init_(department_name, head_of_department, number_of_employees)
        self.recruitment_status = recruitment_status

    def recruitment_info(self):
        print(f"Recruitment Status: {self.recruitment_status}")

    def department_info(self):
        super().department_info()
        self.recruitment_info()
        
class Marketing(Department):
    def _init_(self, department_name, head_of_department, number_of_employees, marketing_budget):
        super()._init_(department_name, head_of_department, number_of_employees)
        self.marketing_budget = marketing_budget

    def marketing_budget_info(self):
        print(f"Marketing Budget: ${self.marketing_budget} million")

    def department_info(self):
        super().department_info()
        self.marketing_budget_info()

class Production(Department):
    def _init_(self, department_name, head_of_department, number_of_employees, production_capacity):
        super()._init_(department_name, head_of_department, number_of_employees)
        self.production_capacity = production_capacity

    def production_capacity_info(self):
        print(f"Production Capacity: {self.production_capacity} units/month")

    def department_info(self):
        super().department_info()
        self.production_capacity_info()
        
hr_department = HR("Human Resources", "mouna", 15, "Active Recruitment")
marketing_department = Marketing("Marketing", "mouni", 20, 5)
production_department = Production("Production", "mona", 50, 2000)

print("HR Department Information:")
hr_department.department_info()
print("\nMarketing Department Information:")
marketing_department.department_info()
print("\nProduction Department Information:")
production_department.department_info()
