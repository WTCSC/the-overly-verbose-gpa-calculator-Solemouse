# Validates that the grades are between 0 and 4 and if not then it asks for a new input
def valid(prompt):
    while True:
        try:
            grade = float(input(prompt))
            if 0.0 <= grade <= 4.0:
                return grade
            else:
                print("Sorry, grades have to be between 0.0 and 4.0")
        except ValueError:
            print("Sorry, cant do that, invalid input")

# Checks that the grades and greater than 0 and if not then it asks for a new input
def pos_int(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num > 0:
                return num
            else:
                print("Sorry Bud, cant be zero")
        except ValueError:
            print("Sorry Bud, cant be that number")

# Calculates the gpa with the sum of the grade list and the length of the grade list
def calc(grade_list):
    return sum(grade_list) / len(grade_list)


print("Welcome to a GPA calculator, where you can get disappointed in your life in a few easy steps, or well, if you have a low gpa, then maybe not so easy")
how_many = pos_int("\nHow many classes or grades would you like to add to your disappointment ")

grades = []
print(f"\nPlease enter your {how_many} grades as a number 0.0 through 4.0")

# Asks for the grades and appends it to a list
for i in range(how_many):
    grade = valid(f" - Enter grade for class #{i + 1}: ")
    grades.append(grade)

# Calculates the gpa with the defined calc function 
current = calc(grades)
print(f"\nYour current GPA is this, is that good? {current:.2f}")

print("\nLets see if your performance is disappointment worthy")
half = len(grades) // 2

# Checks if you only entered one class and if you want to analyze the first half or second half of the grades
if len(grades) == 1:
    print("Damn, only one class?")
else:
    choice = input("Would you like to analyze the 'first' half or 'second' half of your disappointment? ").strip().lower()
    # Checks if the choice starts with f or s then sets the semester_grades to either first half or second half depending on input
    if choice.startswith("f"):
        semester_grades = grades[:half]
        semester_name = "first"
    elif choice.startswith("s"):
        semester_grades = grades[half:]
        semester_name = "second"
    else:
        print("Invalid choice, you now only get the first half")
        semester_grades = grades[:half]
        semester_name = "first"

    semester_gpa = calc(semester_grades)
    print(f"\nYour {semester_name} semester disappointment is: {semester_gpa:.2f}")

    if semester_gpa > current:
        print("Nice, your disappointment can go away now")
    elif semester_gpa < current:
        print("Your gpa is terrible and my day is ruined")
    else:
        print("Thats okay, I guess")

goal = valid("\nGoal? Do you want to set a goal? Alright, what gpa do you want")

# Checks if the gpa you want is acheivable with only raising 1 grade to a 4 
if goal <= current:
    print(f"Your current grades of {current:.2f} already meets or exceeds your disappointment")
else:
    print(f"\nAnalyzing the fewer and fewer possibilities to lower your dissapointment of {goal:.2f}...")
    achievable = False
    for i in range(len(grades)):
        new_grades = grades.copy()
        new_grades[i] = 4.0
        new_gpa = calc(new_grades)

        if new_gpa >= goal:
            print(f"If you raise whatever class #{i + 1} is, to a 4.0, your GPA would be {new_gpa:.2f}.")
            achievable = True

    if not achievable:
        print("Your lack of disappointment isn't reachable by improving just one grade.")
        print("You'll need to boost multiple grades to not be disappointed")

print("\nThanks for measuring your disappointment")
