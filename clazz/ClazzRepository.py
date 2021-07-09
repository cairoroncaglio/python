from mongoConn import MongoConnection


def getcollection(): return MongoConnection.getCollection('clazz')


def insert(clazz): return getcollection().insert_one(clazz)


def findall(): return getcollection().find()


def delete(clazz): return getcollection().delete_one({'name': clazz.name, 'text': clazz.text})
