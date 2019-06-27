from datetime import datetime
class Employee:
	def __init__(self,name,age,salery,employment_date):
		self.name = name
		self.age = age
		self.salery = salery
		self.employment_date = datetime.strptime(employment_date,"%Y-%m-%d")
	def get_working_years(self):
		t = datetime.today().year
		i = datetime.date(self.employment_date).year
		x = t - i
		return x
class Manager(Employee):
	def __init__(self,name,age,salery,employment_date,bonus_percentage):
		Employee.__init__(self,name,age,salery,employment_date)
		self.bonus_percentage = bonus_percentage
	def get_bonus(self):
		return self.bonus_percentage * int((self.salery/100))
employees = []
manager = []
def add_employee():
	a = input("name: ")
	b = input("age: ")
	c = input("salery: ")
	d = input("employment date: ")
	employees.append(Employee(a,b,c,d))
	print("Employee added successfully")

def add_manager():
	a = input("name: ")
	b = input("age: ")
	c = input("salery: ")
	d = input("employment date: ")
	e = input("bonus percentage: ")
	managers = Manager(a,b,c,d,e)
	print("Manager added successfully")
add_employee()
print(employees)