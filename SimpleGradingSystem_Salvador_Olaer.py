firstname = input(str("Input your first name: "))
middlename = input(str("Input your middle initial: "))
lastname = input(str("Input your last name: "))
idnum = int(input("Input your ID#: "))
course = input(str("Input your course: "))
section = input(str("Input your section: "))
firstq = float(input("Input your first quarter grade: "))
secondquar = float(input("Input your second quarter grade: "))
thirdquar = float(input("Input your third quarter grade: "))
fourthquar = float(input("Input your fourth quarter grade: "))

average = firstq + secondquar + thirdquar + fourthquar / 4

name = f"{firstname} {middlename} {lastname}"

print("Name: " + name)
print("ID #: " + str(idnum))
print("Course: " + course)
print("Section: " + section)
print("Your general average is: " + str(average))
