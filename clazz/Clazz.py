from dataclasses import dataclass


@dataclass
class Clazz:
    def __init__(self, name, text):
        self.name = name
        self.text = text

    def tostring(self): return '{name:' + self.name + ', text:' + self.text + '}'

    def bson(self): return {"name": str(self.name), "text": str(self.text)}

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setText(self, text):
        self.text = text

    def getText(self):
        return self.text

    def toObject(self, bson):
        self.name = bson.get('name')
        self.text = bson.get('text')
