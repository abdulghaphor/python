import datetime, math

def check_birthdate(c1,c2,c3):
	t = datetime.date.today()
	i = datetime.date(year = c1,month = c2,day = c3)
	if t > i:
		return True
	else:
		return False
def calculate_age(a,b,c):
	t = datetime.date.today()
	i = datetime.date(year = a,month = b,day = c)
	x = t - i
	yy = math.floor(x.days / 365)
	mm = math.floor((x.days % 365) / 30)
	dd = (x.days % 365) % 30
	print("You are %s years, %s months, and %s days" % (yy,mm,dd))

y = int(input("Enter year of birth: "))
m = int(input("Enter month of birth: "))
d = int(input("Enter day of birth: "))
if check_birthdate(y,m,d) == True:
	calculate_age(y,m,d)
else:
	print("ERROR!")