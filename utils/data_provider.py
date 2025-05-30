from classes.pessoa_class import Pessoa
class DataProvider():

    def __init__(self):
        self.faker = Faker()
        return True
    
    def Pessoa(self):
        return Pessoa