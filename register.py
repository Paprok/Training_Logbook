import os.path
import os

class User():
    def __init__(self):
        self.profile_exists = False
        if self.profile_exists is False:
            self.name = input("Name: ")
            self.surname = input("Surname: ")
            self.file_name = "users/" + self.name.upper() + "_" + self.surname.upper() + ".txt"
            if os.path.exists(self.file_name):
                print("User already exists, log in or register new account.")
                self.profile_exists = True
            else:
                self.password = self.create_password()
                self.gender = self.get_gender()
                self.age = self.assign_int("age")
                self.weight = self.assign_int("weight")
                self.goals = self.choose_goals()

    def get_data_from_user(self, data_type):
        user_data = input(data_type)
        return user_data

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_password(self):
        return self.password

    def get_gender(self):
        gender_ok = None
        while gender_ok is None:
            gender = input("Choose your gender ((type 'female' or 'male') : ")
            if gender.lower() == "male" or gender.lower() == "female":
                return gender
                gender_ok = True
            else:
                print("Unknown choice, try again.")

    def change_name(self, new_name):
        self.name = new_name

    def create_password(self):
        password_ok = None
        while password_ok is None:
            user_password = input("Type your password: ")
            user_password_check = input("Check your password: ")

            if user_password == user_password_check:
                return user_password
                password_ok = True
            else:
                print("Password is not correct, try again.")

    def choose_goals(self):
        goals = {1: 'lose body fat', 2: 'hypertrophy', 3: 'strength'}
        print("Choose your goal: ", goals)

        goal_choosen = False
        while goal_choosen is False:
            choose = int(input("Type number of goal: "))
            if choose in (1, 2, 3):
                goal_choosen = True
                return goals[choose]
            else:
                print("Unknown choice, try again.")

    def assign_int(self, value_name):
        is_int = False
        while is_int is False:
            number = input("Type your " + value_name + ": ")
            if number.isdigit():
                return number
                is_int = True
            else:
                print("It's not a number!")

    def user_data_to_export(self):
        return "\t".join(string for string in [self.name,
                                               self.surname,
                                               self.password,
                                               self.gender,
                                               str(self.age),
                                               str(self.weight),
                                               self.goals])

    def tests_to_export(self):
        tests_to_export = "#0\t".join(exercise for exercise in ['Squat',
                                                                'Dead Lift',
                                                                'Millitary Press',
                                                                'Bench Press',
                                                                'Pull Ups',
                                                                'Run 5km'])
        tests_to_export = tests_to_export + "#0"
        return tests_to_export

    def export_data(self):
        with open(self.file_name, "w") as data_file:
            data_file.write(self.user_data_to_export() + "\n" + self.tests_to_export())


def start_module():
    os.system('clear')
    user = User()
    os.system('clear')
    if not user.profile_exists:
        user.export_data()
