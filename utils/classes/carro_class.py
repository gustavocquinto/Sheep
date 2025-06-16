from core.autoload import faker
from faker_vehicle import VehicleProvider
class Carro():
    def __init__(self):
        self.faker = faker
        self.faker.add_provider(VehicleProvider)

        self.nome = faker.vehicle_year_make_model()
        self.ano = faker.machine_year()
        self.categoria = faker.machine_category()
