from faker import Faker
import random
class Pessoa():

    def __init__(self):
        fake = Faker('pt_BR')
        self.nome=fake.first_name()
        self.sobrenome=fake.last_name()
        self.sexo = random.choice(['homem, mulher, outro'])
        self.email=fake.email()
        self.cpf=fake.cpf()
        self.telefone=random.randint(1000000000, 9999999999)
        self.endereco=fake.address()

