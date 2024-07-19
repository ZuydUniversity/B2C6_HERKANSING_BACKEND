class TemplateModel:
    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address

    def getmodel(self):
        return {self.id, self.name, self.address}
