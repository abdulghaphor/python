skills = ["python","writing","sleeping","coding"]
print("Welcome to the special recruitment program, please answer the following questions:")
name = input("name: ")
age = input("age: ")
experience = input("how many years of experience do you have? ")
i = 0
for skill in skills:
	i += 1
	print(i,skill)
s1 = input("choose a skill from above: ")
s2 = input("choose another skill from above: ")

cv = {
	"name" : name,
	"age" : age,
	"experience" : experience,
	"skills" : [s1,s2]
}
print(cv)
if (int(cv["age"]) > 21) and (int(cv["experience"]) > 5) and ("1" in cv["skills"]):
	print("you have been accepted,", cv["name"])
else:
	print("REJECTED,", cv["name"])