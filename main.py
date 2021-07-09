from clazz import ClazzConverter, ClazzRepository, Clazz, ClazzPersistenceAdapter
from clazz import ClazzDto


def finduserbyname(clazzList, name):
    for clazz in clazzList:
        if (clazz.name == name):
            return clazz;


def loop():
    return input('CRUD:\n 1-Salvar novo usuário \n 2-Achar todos usuários\n 3-Delete usuário')


if __name__ == '__main__':
    op1 = loop()

if (op1 == '1'):
    userName = input('Digite o nome do usuário:')
    clazz = Clazz.Clazz(str(userName), 'empty')
    user = ClazzPersistenceAdapter.insert(clazz.bson())
    print('Usuário cadastrado com sucesso')

if (op1 == '2'):
    clazzList = ClazzPersistenceAdapter.findall()
    print('Número de registros: ' + str(len(clazzList)))
    for clazz in clazzList:
        print(clazz.getName())

if (op1 == '3'):
    clazzList = ClazzPersistenceAdapter.findall()
    print('Usuários disponíveis')
    for clazz in clazzList:
        print(clazz.getName())

    username = input('Qual usuário você deseja remover? Digite o nome do usuário')
    user = finduserbyname(clazzList, username)
    ClazzPersistenceAdapter.delete(user)

# clazzDto = ClazzDto.ClazzDto('YAHOOOWW', 'Test class')
# clazz = ClazzConverter.ClazzConverter.toEntity(clazzDto)
# response = ClazzRepository.insert(clazz.bzon())
# ClazzRepository.findAll()
