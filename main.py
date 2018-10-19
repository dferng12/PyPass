from PyPass import *

if __name__ == '__main__':
    option = input('Wanna create new account(1) or login(2) ?')
    pyPass = PyPass()

    if option == '1':
        username = input('Enter username: ')
        masterPass = input('Enter master password: ')
        if not pyPass.create_account(username, masterPass):
            print('Username already exists')
            exit(0)
        else:
            print('Username created successfuly')

    elif option != '1' and option != '2':
        print('Not valid option')
        exit(0)

    username = input('Enter username: ')
    masterPass = input('Enter master password: ')

    if pyPass.auth_user(username,masterPass):
        while True:
            print('--------------')
            print('Options: ')
            print('1: Enter new username/password')
            print('2: Show existing username/password')
            print('3: Generate password for username')
            print('4: Exit')

            choice = input("Enter the number: ")

            if choice == '1':
                id = input('Enter identifier: ')
                username = input('Enter username: ')
                password = input('Enter password: ')

                pyPass.create_entry(id, username, password)

            elif choice == '2':
                id = input('Enter identifier: ')
                entry = pyPass.get_entry(id)
                print("User: " + entry['username'].decode('UTF-8'))
                print("Password: " + entry['password'].decode('UTF-8'))

            elif choice == '3':
                id = input('Enter identifier: ')
                username = input('Enter username: ')
                pyPass.generate_new_entry(id, username)

            elif choice == '4':
                exit(0)
            else:
                print('Not valid number')

    else:
        print('Username or password wrong. Exiting.')
