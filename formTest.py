from AutomationController import AutomationController
from config import *
from time import *
import random
class FormTest:
    def __init__(self):
        self.cmd = AutomationController()
        self.cmd.acessaSite(url_app)

    def preencheFormularioCorretamente(self):
        self.cmd.buscaElemento("firstName", "id").preencher("Gustavo")
        
        self.cmd.buscaElemento("lastName", "id").preencher("Quinto")

        self.cmd.buscaElemento("userEmail", "id").preencher("gustavo@teste.com")

        randomico = random.randint(1, 3)
        self.cmd.buscaElemento(f'label[for="gender-radio-{randomico}"]', "css_selector").clicar()

        sleep(10)


