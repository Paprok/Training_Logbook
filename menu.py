import log_in
import register


def start_module():    
    option = 1
    while option != '0':
        print_menu()
        option = input('Please choose option')
        if option == "1":
            # 
        elif option == "2":
            #            
        elif option == "3":
            #             
        elif option == "4":
            #             
        elif option == "5":
            # 
        elif option == "6":
            #
        elif option == "0":
            print('Thanks for using our training programm! Good luck!')
            # funkcja do zapisania danych?
        else:
            raise KeyError("There is no such option.")


def print_menu():
    print('1. Generate your training session')
    print('2. ')