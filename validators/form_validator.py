
from core.autoload import AutomationController
from utils.classes.pessoa_class import Pessoa

class formValidator():
    def __init__(self, automationController: AutomationController):
        self.cmd = automationController

    def validar_preenchimento_formulario(self, dados):
        self.pessoa: Pessoa = dados[0]
        
        self.cmd.buscar_elemento("firstName", "id").validar(self.pessoa.nome)