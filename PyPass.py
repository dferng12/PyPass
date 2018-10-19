from Entry import Entry
from SecurityManager import SecurityManager
from DBController import DBController


class PyPass:
    def __init__(self):
        self.__dbController = DBController('localhost', 27017)

    def set_username(self, username):
        hashedUsername = SecurityManager.get_hash(username)
        self.__username = hashedUsername
        self.__dbController.set_username(hashedUsername)

    def store_entry(self, id, ciphered_user, ciphered_pass):
        new_entry = Entry(id, ciphered_user, ciphered_pass)
        self.__dbController.storeEntry(new_entry)

    def get_entry(self, identifier):
        entry = self.__dbController.getEntry(SecurityManager.get_hash(identifier))
        username = self.__securityManager.decipher_field(entry.username)
        password = self.__securityManager.decipher_field(entry.password)

        return {'identifier': identifier, 'username': username, 'password': password}

    def create_entry(self, id, username, password):
        ciphered_user = self.__securityManager.cipher_field(username)
        ciphered_password = self.__securityManager.cipher_field(password)
        hashed_id = SecurityManager.get_hash(id)
        self.store_entry(hashed_id, ciphered_user, ciphered_password)

    def generate_new_entry(self, id, username):
        ciphered_user = self.__securityManager.cipher_field(username)
        ciphered_pass = self.__securityManager.generate_password()
        ciphered_id = self.__securityManager.cipher_field(id)
        self.store_entry(ciphered_id, ciphered_user, ciphered_pass)

    def create_account(self, username, masterPass):
        hashedUsername = SecurityManager.get_hash(username)
        hashedMasterPass = SecurityManager.get_hash(SecurityManager.get_hash(masterPass))
        return self.__dbController.createUser(hashedUsername, hashedMasterPass)

    def auth_user(self, username, masterPass):
        hashedUsername = SecurityManager.get_hash(username)
        hashedMasterPass = SecurityManager.get_hash(SecurityManager.get_hash(masterPass))
        if self.__dbController.authUser(hashedUsername, hashedMasterPass):
            self.__dbController.set_username(hashedUsername)
            self.__securityManager = SecurityManager(masterPass)
            return True
        else:
            return False

