# dictionary list of student info
students = [
    {"name": "Tina", "hometown": "Chicago", "favorite food": "Banana"},
    {"name": "Kyra", "hometown": "Detroit", "favorite food": "Pancakes"},
    {"name": "Brittany", "hometown": "Denver", "favorite food": "Dirt"},
    {"name": "Bernie", "hometown": "Phoenix", "favorite food": "Spaghetti"},
    {"name": "Tree", "hometown": "Salt Lake City", "favorite food": "Deer Meat"}
]


# Function to list names of students
def list_names(students):
    index = 1  # index starts at 1
    for particular_student in students:
        print(f"{index}. {particular_student['name']}")
        index += 1  # index adds 1 to each new name in list


# Function get_new_student to add a new student
def get_new_student():
    new_student_name = input("Enter student name:\n> ")
    new_student_hometown = input("Next enter their hometown:\n> ")
    new_student_favorite_food = input("Last please enter their favorite food:\n> ")
    return {"name": new_student_name, "hometown": new_student_hometown, "favorite food": new_student_favorite_food}


# Main Loop
while True:
    # ask user whether they would like to select one of the following options
    options = input("Which of the following options would you like to do: add, view, or quit\n> ")

    # using our get_new_student that was previously created
    if options == "add":
        new_student = get_new_student()
        students.append(new_student)
        print("New student added successfully!")
    # Will have to nest to incorporate info about hometown and favorite food
    elif options == "view":
        list_names(students)
        student_select = int(
            input(f"Which student would you like to learn more about? Enter a number 1-{len(students)}\n> "))
        if 1 <= student_select <= len(students):
            selected_student = students[student_select - 1]
            print("Student name:", selected_student["name"])
            selection = input("What would you like to know?\nEnter hometown or favorite food\n> ")
            if selection == "hometown":
                print(f"Hometown: {selected_student['hometown']}")
            elif selection == "favorite food":
                print(f"Favorite food: {selected_student['favorite food']}")
            else:
                print("Not a valid option")
        else:
            print("Not a valid option")
    elif options == "quit":
        print("Peace out! Have a nice life <3")
        break
    # occurs when NOT one of the three options, and re-prompts
    else:
        print("Not a valid option, please try again")
