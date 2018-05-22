class User():
    def __init__(self):
        self.name = input("Name: ")
        self.surname = input("Surname: ")
        self.password = self.create_password()
        self.gender = self.get_gender()
        self.age = input("Age: ")
        self.file_name = "users/" + self.name.upper() + "_" + self.surname.upper() + ".txt"
        self.test_result = [
            'Squat': 0,
            'Dead Lift',
            'Millitary Press',
            'Bench Press',
            'Pull Ups',
            'Run 5km'
        ]

    def get_data_from_user(self, data_type):
        user_data = input(data_type)
        return user_data

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_password(self):
        return self.password

    def find_user_data_file(self):
        name = input("Your name: ")
        surname = input("Your surname: ")
        filename = "users/" + name.upper() + "_" + surname.upper() + ".txt"
        try:
            with open(filename, "r") as user_data_file:
                return True
        except:
            return False

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

    def user_data_to_export(self):
        return "\t".join(string for string in [self.name,
                                               self.surname,
                                               self.password,
                                               self.gender,
                                               self.age])

    def export_data(self):
        with open(self.file_name, "w") as data_file:
            data_file.write(self.user_data_to_export())


def main():
    dupa = User()
    print(dupa.file_name)
    print(dupa.user_data_to_export())
    print(dupa.find_user_data_file())
    dupa.export_data()


main()
