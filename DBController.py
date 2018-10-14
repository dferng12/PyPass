from pymongo import MongoClient

from Entry import Entry


class DBController:

    def __init__(self, db_url, port, username):
        self.client = MongoClient(db_url, port)
        self.db = self.client['pypass']
        self.username = username

    def store(self, newEntry):
        json_entry = {'_id': newEntry.identifier, 'username': newEntry.username, 'password': newEntry.password}
        collection = self.db[self.username]
        collection.insert_one(json_entry)

    def get(self, identifier):
        collection = self.db[self.username]
        entryData =  collection.find_one({"_id": identifier})
        entry = Entry(entryData['_id'], entryData['username'], entryData['password'])
        return entry


