from pymongo import MongoClient


def connectionDb():
    mongoClient = MongoClient('mongodb://localhost:27017/')
    return mongoClient['python-project']


def getCollection(collectionName):
    connection = connectionDb()
    return connection[str(collectionName)]
