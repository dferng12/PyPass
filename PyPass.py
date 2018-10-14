from Entry import Entry
from SecurityManager import SecurityManager
from DBController import DBController


class PyPass:
    def __init__(self, username, master_password):
        self.__username = username
        self.__securityManager = SecurityManager(master_password)
        self.__dbController = DBController('localhost', 27017, username)

    def check_master_password(self):
        return True

    def store_entry(self, id, ciphered_user, ciphered_pass):
        new_entry = Entry(id, ciphered_user, ciphered_pass)
        self.__dbController.store(new_entry)

    def get_entry(self, identifier):
        entry = self.__dbController.get(identifier)
        username = self.__securityManager.decipher_field(entry.username)
        password = self.__securityManager.decipher_field(entry.password)

        return {'identifier': entry.identifier, 'username': username, 'password': password}

    def create_entry(self, id, username, password):
        ciphered_user = self.__securityManager.cipher_field(username)
        ciphered_password = self.__securityManager.cipher_field(password)
        self.store_entry(id, ciphered_user, ciphered_password)

    def generate_new_entry(self, id, username):
        ciphered_user = self.__securityManager.cipher_field(username)
        ciphered_pass = self.__securityManager.generate_password()
        self.store_entry(id, ciphered_user, ciphered_pass)