class Entity:
    def __init__(self, name, fields):
        self.name = name
        self.fields = fields

    def printFields(self):
        for field in self.fields:
            print(field.name)