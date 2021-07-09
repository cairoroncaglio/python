class ClazzDto:
    def __init__(self, nameDto, textDto):
        self.nameDto = nameDto
        self.textDto = textDto

    def tostring(self): return '{' + self.nameDto + ', ' + self.textDto + '}'
