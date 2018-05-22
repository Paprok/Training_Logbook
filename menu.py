import log_in
import register
import test


def start_module(user):    
    option = 1
    while option != '0':
        print_menu()
        option = input('\nPlease choose option: ')
        if option == "1":
            test.start_module(user)
        # elif option == "2":
        #     # profile         
        # elif option == "3":
        #     # create training session          
        # elif option == "4":
        #     # start/ check traingin
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
    print('2. Generate your training session')