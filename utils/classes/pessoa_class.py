from core.autoload import faker
import random
class Pessoa():

    def __init__(self):
        self.nome=faker.first_name()
        self.sobrenome=faker.last_name()
        self.genero = random.choice(['homem, mulher, outro'])
        self.email=faker.email()
        self.cpf=faker.cpf()
        self.telefone=random.randint(1000000000, 9999999999)
        self.endereco=faker.address()

