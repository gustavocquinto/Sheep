from core.autoload import AutomationController
from selenium.webdriver.common.by import By
from core.asserts_controller import Asserts


class TextBoxValidator():
    def __init__(self, automationController: AutomationController):
        self.cmd = automationController
        self.asserts = Asserts()
        return None
    

    def validar_preenchimento(self, dados):

        self.id_campos = ["name", "email", "currentAddress", "permanentAddress"]


        for i, dado in enumerate(dados):
            elemento = self.cmd.buscar_elemento(self.id_campos[i], "id")
            self.asserts.checar(dado, elemento.texto())

        self.asserts.relatorio_asserts(self.validar_preenchimento.__qualname__)
        return None