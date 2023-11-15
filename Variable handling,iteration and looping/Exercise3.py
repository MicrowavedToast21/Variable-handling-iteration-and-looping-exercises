from datetime import date

year = int(input("Enter your year of birth: "))
month = int(input("Enter your month of birth: "))
day = int(input("Enter your day of birth: "))
def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age
print(calculateAge(date(year, month, day)), "years old")
