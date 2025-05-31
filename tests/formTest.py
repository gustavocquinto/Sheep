from core.automation_controller import AutomationController
from config.settings import *
from utils.data_provider import DataProvider
from time import *
import random
class FormTest:
    def __init__(self):
        self.cmd = AutomationController()
        self.data_provider = DataProvider()

        self.cmd.acessaSite(url_app)

    def preencheFormularioCorretamente(self):
        self.pessoa = self.data_provider.Pessoa()

        self.cmd.buscaElemento(f"firstName", "id").preencher(f"{self.pessoa.nome}")
        
        self.cmd.buscaElemento("lastName", "id").preencher(f"{self.pessoa.sobrenome}")

        self.cmd.buscaElemento("userEmail", "id").preencher(f"{self.pessoa.email}")

        #Genêro aleatório
        randomico = random.randint(1, 3)
        self.cmd.buscaElemento(f'label[for="gender-radio-{randomico}"]', "css_selector").clicar()

        self.cmd.buscaElemento(f"userNumber", "id").preencher(f"{self.pessoa.telefone}")

        self.cmd.buscaElemento(f"subjectsInput", "id").preencher(f"Computer Science").teclaEnter()

        randomico = randomico
        self.cmd.buscaElemento(f'label[for="hobbies-checkbox-{randomico}"]', "css_selector").clicar()

        sleep(10)


