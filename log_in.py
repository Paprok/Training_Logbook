class User():
    def __init__(self, data_list):
        pass


def find_user_data_file():
    name = input("Your name: ")
    surname = input("Your surname: ")
    filename = "users/" + name.upper() + "_" + surname.upper() + ".txt"
    try:
        with open(filename, "r") as user_data_file:
            return True
    except:
        find_user_data_file()


def main():
    find_user_data_file()





main()

