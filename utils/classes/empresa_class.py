from core.autoload import faker
class Empresa():
    def __init__(self):
        self.nome = faker.company()
        self.endereco = faker.address()
        self.cnpj = faker.cnpj()
        self.id = faker.company_id()
        self.slogan = faker.catch_phrase()