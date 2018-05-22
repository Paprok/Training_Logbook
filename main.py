import log_in
import register
import menu
import sys
import os


def main():
    while True:
        handle_menu()
        try:
            choose()
        except KeyError:
            print('Wrong Key!!!')
       

def choose():
    'choses from options'
    option = input("Please choose position from menu: ")
    if option == "1":
        # log in function
    elif option == "2":
        # register function
    elif option == "0":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")


def handle_menu():
    print('1. Log in')
    print('2. Register')


if __name__ == '__main__':
    main()
