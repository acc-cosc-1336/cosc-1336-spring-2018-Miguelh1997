from employee import Employee
class HourlyEmployee(Employee):
    
    def __init__(self,employee_id, name, hourly_rate,worked_hours):
        Employee.__init__(self,employee_id,name,hourly_rate,worked_hours)
        self.hourly_rate = hourly_rate
        self.worked_hours = worked_hours

    def calculate(self):
        return self.worked_hours * self.hourly_rate
