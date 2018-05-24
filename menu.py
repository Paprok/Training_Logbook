import log_in
import register
import test
import training
import os
# import log


def start_module(user):
    option = 1
    while option != '0':
        print_menu()
        option = input('\nPlease choose option: ')
        if option == "1":
            test.start_module(user)
        elif option == "2":
            show_profile(user)
        elif option == "3":
            training.start_module(user)
        elif option == "4":
            log.start_module(user)
        # elif option == "5":
        #     # 
        # elif option == "6":
        #     #
        elif option == "0":
            print('Thanks for using our training programm! Good luck!')
            user.save_user_data(user.data_file_name)
        else:
            raise KeyError("There is no such option.")


def print_menu():
    print('\nMain Menu:')
    print('1. Test Menu ')
    print('2. Show profile')
    print('3. Create Training Session')
    print('4. Show/ Start Training')
    print('0. Log out')


def show_profile(user):
    os.system('clear')
    profile_information = ["Name: ", "Surname: ", "Password: ", "Gender: ", "Age: ", "Weight: ", "Goal: "]
    user_data = user.data_list
    test_result = user.test_result

    print("\nUser profile:\n")

    for item in range(len(profile_information)):
        if profile_information[item] == "Password: ":
            print(profile_information[item], "*" * len(user_data[item]))
        else:
            print(profile_information[item], user_data[item])

    print("\nUser's test results:\n")

    for key, value in test_result.items():
        print(key, value)

    input("\nEnter to continue...")
