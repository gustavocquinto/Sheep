from faker import Faker
class Pessoa():

    def __init__(self):
        fake = Faker()
        self.nome=fake.name()
        self.email=fake.email()
        self.cpf=fake.cpf()
        self.telefone=fake.phone_number()
        self.endereco=fake.address()

