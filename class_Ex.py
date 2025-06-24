class Employee:
    def __init__(self, name, salary, phone, email):
        self.name = name
        self.salary = salary
        self.phone = phone
        self.email = email

    def display_info(self):
        print("Employee Information:")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Salary: ${self.salary:.2f}")

# Example usage
emp = Employee(name="Sakshi Suryawanshi", salary=72000, phone="7666065200", email="Sakshisuryawanshi2412@gmail.com")
emp.display_info()
