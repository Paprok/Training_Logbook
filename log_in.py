import os.path
import menu


class User():
    def __init__(self, file_name):
        self.data_list = self.open_data(file_name)
        self.name = self.data_list[0]
        self.surname = self.data_list[1]
        self.password = self.data_list[2]
        self.gender = self.data_list[3]
        self.age = self.data_list[4]
        self.weight = self.data_list[5]
        self.goal = self.data_list[6]
        self.test_result = self.get_test_result(file_name)

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

    def get_test_result(self):
        return self.test_result

    def set_test_result(self, key, answer):
        self.test_result[key] = answer

    def open_data(self, file_name):
        with open(file_name, "r") as user_data_file:
            user_data = user_data_file.readlines()
        return user_data[0].split("\t")

    def get_test_result(self, file_name):
        with open(file_name, "r",) as user_data_file:
            reader = user_data_file.readlines()
            user_test_list = reader[1].split("\t")
            user_test_dict = {}

            for test in user_test_list:
                test_and_score = test.split("#")
                print(test_and_score)
                user_test_dict[test_and_score[0]] = test_and_score[1]
            print(user_test_dict)

        return user_test_dict

    # ?????????? funkcja ktora zmienia dany atrybut classy User (do uzycia przy tescie), 
    # funkcja ktora zbiera wszystkie dane i nadpisuje plik users/imie_nazwisko.txt
    # uzyc ja do zapisu po wyjsciu
    #


def find_user_data_file():
    print('\nPlease enter your login data!')
    tries = 3
    while tries > 0:
        name = input("Your name: ")
        surname = input("Your surname: ")
        file_name = "users/" + name.upper() + "_" + surname.upper() + ".txt"
        if os.path.exists(file_name):
            return file_name
            tries = 0
        else:
            tries -= 1


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
    if user_data_file is not None:
        user_data_list = get_user_data_list(user_data_file)
        if check_password(user_data_list):
            user = User(user_data_file)
            print(user.data_list)
            menu.start_module(user)


# # module start menu
#start_module()
