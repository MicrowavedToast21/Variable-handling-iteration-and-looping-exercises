while True:
    try:
      theory_grade = float(input("Enter your theory grade: "))
      if theory_grade < 0 or theory_grade > 10:
         print("Please enter a number between 0 and 10: ")
      break
    except ValueError:
        print("Please enter an actual number: ")

while True:
    try:
      practical_grade = float(input("Enter your practical grade: "))
      if practical_grade < 0 or theory_grade > 10:
          print("Please enter a number between 0 and 10: ")
      break
    except ValueError:
        print("Please enter an actual number: ")

final_grade = theory_grade*0.6 + practical_grade*0.4
def final_grade_calculator(final_grade):
    if final_grade >=9:
        print("Your final grade is: ", final_grade, "Outstanding!")
    elif final_grade >= 7:
        print("Your final grade is: ", final_grade, "Notable!")
    elif final_grade >= 5:
        print("Your final grade is: ", final_grade, "Pass!")
    else:
        print("Your final grade is: ", final_grade, "Fail!")
final_grade_calculator(final_grade)
