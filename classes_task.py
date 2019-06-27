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
print("Welcome to HR Pro 2019\nChoose an action to do:\n \t1. show employees\n\t2. show managers\n\t3. add an employee\n\t4. add a manager\n\t5. exit\n")

employees = [
Employee("Abdulghaphor Hajjieh",31,1000,"2017-03-03"),
Employee("Fatma Nouraldeen",27,2000,"2015-04-27"),
Employee("Meshari Al Obaidi",29,3500,"2012-01-21")
]

managers = [
Manager("Abdulhameed Hussain",55,5000,"1980-10-04",5),
Manager("Mohammed Al Enezi",54,4000,"1983-04-04",3),
Manager("Mohammad Ramadhan",43,3000,"1994-04-21",2.5)
]

def show_employees():
	print("We have the following employees:")
	for employee in employees:
		print("\tName: %s, Age %s, Salery: %s, Years: %s" % (employee.name,employee.age,employee.salery,employee.get_working_years()))
	print("End of employees list\n")

def show_managers():
	print("We have the following managers:")
	for manager in managers:
		print("\tName: %s, Age %s, Salery: %s, Years: %s, Bonus Percentage: %s" % (manager.name,manager.age,manager.salery,manager.get_working_years(),manager.bonus_percentage))
	print("End of managers list\n")

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
	managers.append(Manager(a,b,c,d,e))
	print("Manager added successfully")


x = "start"
t = 0
while x:
	x = input("What would you like to do ?")
	if x=="1":
		show_employees()
	elif x=="2":
		show_managers()
	elif x=="3":
		add_employee()
	elif x=="4":
		add_manager()
	elif x=="5":
		print("Thank you for using HR Pro 2019.")
		break
	else:
		t += 1
		if t > 3: break
		print("Invalid Entry.")
		continue
