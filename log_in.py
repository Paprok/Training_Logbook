import os.path
import menu


class User():
    def __init__(self, file_name):
        self.data_file_name = file_name
        self.data_list = self.open_data(file_name)
        self.name = self.data_list[0]
        self.surname = self.data_list[1]
        self.password = self.data_list[2]
        self.gender = self.data_list[3]
        self.age = self.data_list[4]
        self.weight = self.data_list[5]
        self.goal = self.data_list[6]
        self.test_result = self.create_test_result(file_name)

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

    def create_test_result(self, file_name):
        with open(file_name, "r",) as user_data_file:
            reader = user_data_file.readlines()
            user_test_list = reader[1].split("\t")
            user_test_dict = {}

            for test in user_test_list:
                test_and_score = test.split("#")
                # print(test_and_score)
                user_test_dict[test_and_score[0]] = test_and_score[1]
            # print(user_test_dict)

        return user_test_dict

    def data_list_to_string(self, data_list):
        data_string = ''

        for data in data_list:
            data_string += data + '\t'

        data_string = data_string[:-1]

        return data_string

    def test_result_to_string(self, test_result):
        test_result_string = ''

        for key, value in self.test_result.items():
            test_result_string += key + "#" + value + "\t"
        test_result_string = test_result_string[:-1]

        return test_result_string

    def save_user_data(self, data_file_name):
        with open(data_file_name, "w") as data_file:
            data_file.write(self.data_list_to_string(self.data_list) + self.test_result_to_string(self.test_result))


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
