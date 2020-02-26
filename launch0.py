name=str(input("Enter your name"))
firstAndLastName=name.split(" ")
age=int(input("Enter your age"))
currentYear=2020
hundred=(100-age)
year=hundred+currentYear
print("Hey "+firstAndLastName[0]+" ! You'll turn 100 years old in ",year)
