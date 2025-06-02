from core.autoload import AutomationController
from config.settings import *
from utils.data_provider import DataProvider
from validators.form_validator import formValidator
from time import *
import random
class FormTest:
    def __init__(self):
        self.cmd = AutomationController()
        self.data_provider = DataProvider()
        self.formValidator = formValidator(self.cmd)
        self.dados = []
        self.cmd.acessaSite(url_app)

    def preencheFormularioCorretamente(self):
        self.pessoa = self.data_provider.Pessoa()
        self.dados.append(self.pessoa)

        self.cmd.buscar_elemento(f"firstName", "id").preencher(f"{self.pessoa.nome}")
        
        self.cmd.buscar_elemento("lastName", "id").preencher(f"{self.pessoa.sobrenome}")

        self.cmd.buscar_elemento("userEmail", "id").preencher(f"{self.pessoa.email}")

        #Genêro aleatório
        randomico = random.randint(1, 3)
        self.cmd.buscar_elemento(f'label[for="gender-radio-{randomico}"]', "css_selector").clicar()

        self.cmd.buscar_elemento(f"userNumber", "id").preencher(f"{self.pessoa.telefone}")

        self.cmd.buscar_elemento(f"subjectsInput", "id").preencher(f"Computer Science").teclaEnter()

        randomico = randomico
        self.cmd.buscar_elemento(f'label[for="hobbies-checkbox-{randomico}"]', "css_selector").clicar()


        self.formValidator.validar_preenchimento_formulario(self.dados)
        sleep(10)


