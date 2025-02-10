class Dept:
    def _init_(self, name):
        self.name = name

    def display_info(self):
        print(f"This is the {self.name} department.")

# Subclass: HR
class HR(Dept):
    def _init_(self):
        super()._init_("HR")

    def recruit_employee(self, candidate_name):
        print(f"Recruiting {candidate_name} into the company.")

    def manage_employee_records(self):
        print("Managing employee records.")

# Subclass: Marketing
class Marketing(Dept):
    def _init_(self):
        super()._init_("Marketing")

    def run_campaign(self, campaign_name):
        print(f"Running marketing campaign: {campaign_name}.")

    def analyze_market_trends(self):
        print("Analyzing market trends.")

# Subclass: Production
class Production(Dept):
    def _init_(self):
        super()._init_("Production")

    def manage_production_line(self):
        print("Managing the production line.")

    def maintain_quality(self):
        print("Ensuring product quality.")

# Example usage
if _name_ == "_main_":
    hr_dept = HR()
    hr_dept.display_info()
    hr_dept.recruit_employee("Alice")
    hr_dept.manage_employee_records()

    marketing_dept = Marketing()
    marketing_dept.display_info()
    marketing_dept.run_campaign("New Product Launch")
    marketing_dept.analyze_market_trends()

    production_dept = Production()
    production_dept.display_info()
    production_dept.manage_production_line()
    production_dept.maintain_quality()
