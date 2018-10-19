from pymongo import MongoClient

from Entry import Entry


class DBController:

    def __init__(self, db_url, port):
        self.client = MongoClient(db_url, port)
        self.db = self.client['pypass']

    def set_username(self, hashedUsername):
        self.hashedUsername = hashedUsername

    def storeEntry(self, newEntry):
        json_entry = {'_id': newEntry.identifier, 'username': newEntry.username, 'password': newEntry.password}
        collection = self.db[self.hashedUsername]
        collection.insert_one(json_entry)

    def getEntry(self, identifier):
        collection = self.db[self.hashedUsername]
        entryData =  collection.find_one({"_id": identifier})
        entry = Entry(entryData['_id'], entryData['username'], entryData['password'])
        return entry

    def createUser(self, hashedUser, hashedMasterPass):
        collection = self.db['auth']
        document = collection.find_one({"_id" : hashedUser})
        if document == None:
            newUser = {"_id" : hashedUser, "passwd": hashedMasterPass}
            collection.insert_one(newUser)
            return True
        else:
            return False

    def authUser(self, hashedUser, hashedMasterPass):
        collection = self.db['auth']
        userAuth = collection.find_one({"_id": hashedUser, "passwd": hashedMasterPass})
        if userAuth != None:
            return True
        else:
            return False

