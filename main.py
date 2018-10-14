from PyPass import *

if __name__ == '__main__':
    user = input('Enter user: ')
    masterPass = input('Enter master password: ')

    pyPass = PyPass(user, masterPass)

    if pyPass.check_master_password():
        while True:
            print('--------------')
            print('Options: ')
            print('1: Enter new username/password')
            print('2: Show existing usernames/passwords')
            print('3: Generate password for username')

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

            else:
                print('Not valid number')

    else:
        print('Password wrong. Exiting.')
