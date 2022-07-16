#Drew Schmidt 7/15/22
#Python practice from TCM Security's Python for Behginners Course
#Classes and objects practice

class Employees:

    def __init__(self, name, department, role, salary, years_employed):
        self.name = name
        self.department = department
        self.role = role
        self.salary = salary
        self.years_employed = years_employed

    def eligible_for_retirement(self):
        if self.years_employed >= 20:
            return True
        else:
            return False

