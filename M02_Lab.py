# Author: Your Name
# File Name: Student_GPA.py
# Description: This app accepts student names and GPAs, tests if the student qualifies for the Dean's List or the Honor Roll,
# and prints corresponding messages.

def main():
    print("Welcome to the Student GPA App")

    while True:
        last_name = input("Enter student's last name (Enter 'ZZZ' to quit): ")

        if last_name == 'ZZZ':
            print("Exiting the application. Goodbye!")
            break

        first_name = input("Enter student's first name: ")
        gpa = float(input("Enter student's GPA: "))

        if gpa >= 3.5:
            print(f"{first_name} {last_name} has made the Dean's List!")
        elif gpa >= 3.25:
            print(f"{first_name} {last_name} has made the Honor Roll!")
        else:
            print(f"{first_name} {last_name} does not qualify for Dean's List or Honor Roll.")

if __name__ == "__main__":
    main()
