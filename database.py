import pymongo
import dns


class Database(object):

    # parameters common for all users - shared by all objects
    URI = "mongodb+srv://iv20023:Pppp363&@cluster0-4iffi.mongodb.net/test?retryWrites=true&w=majority"
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['udemy']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)