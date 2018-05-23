import log_in
import register
import test
import training
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
            # funkcja do zapisania danych?
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
    print(user.get_name + user.get_surname)
