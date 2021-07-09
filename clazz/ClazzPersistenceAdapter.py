from clazz import ClazzRepository, Clazz


def insert(clazz):
    return ClazzRepository.insert(clazz)


def findall():
    clazzList = []
    for bson in ClazzRepository.findall():
        clazzList.append(Clazz.Clazz(bson.get('name'), bson.get('text')))
    return clazzList


def delete(clazz):
    return ClazzRepository.delete(clazz)
