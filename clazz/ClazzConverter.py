from clazz import Clazz


class ClazzConverter:
    def toEntity(clazzDto):
        return Clazz.Clazz(str(clazzDto.nameDto), str(clazzDto.textDto))
