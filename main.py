import log_in
import register

def main():
    while True:
        handle_menu()
        try:
            choose()
        except KeyError as err:
            ui.print_error_message(err)


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


if __name__ == '__main__':
    main()