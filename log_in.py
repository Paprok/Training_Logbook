# import menu


class User():
    def __init__(self, file_name):
        self.data_list = self.open_user_data(file_name)
        self.name = self.data_list[0]
        self.surname = self.data_list[1]
        self.password = self.data_list[2]
        self.gender = self.data_list[3]
        self.age = self.data_list[4]
        self.weight = self.data_list[5]
        self.goal = self.data_list[6]
        self.test_result = {
            'Squat': 0,
            'Dead Lift': 0,
            'Millitary Press': 0,
            'Bench Press': 0,
            'Pull Ups': 0,
            'Run 5km': 0
        }

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_password(self):
        return self.password

    def get_gender(self):
        return self.gender

    def get_age(self):
        return self.age

    def open_data(self, file_name):
        with open(file_name, "r") as user_data_file:
            user_data = user_data_file.readlines()
        return user_data[0].split("\t")


def find_user_data_file():
    name = input("Your name: ")
    surname = input("Your surname: ")
    file_name = "users/" + name.upper() + "_" + surname.upper() + ".txt"
    try:
        with open(file_name, "r") as user_data_file:
            return file_name
    except:
        print("Wrong user name or surname, try again.")
        find_user_data_file()


def get_user_data_list(user_data_file):
    with open(user_data_file, "r",) as data_file:
        reader = data_file.readlines()
        user_data_list = reader[0].split("\t")

    return user_data_list


def check_password(user_data_list):
    check_password_tries = 3
    while check_password_tries > 0:
        password = input("Type your password: ")
        if user_data_list[2] == password:
            return True
            check_password_tries = 0
        else:
            print("Wrong password, try again.")
            check_password_tries -= 1


def start_module():
    user_data_file = find_user_data_file()
    user_data_list = get_user_data_list(user_data_file)
    if check_password(user_data_list):
        user = User(user_data_file)
        print(user.data_list)

# module start menu
start_module()