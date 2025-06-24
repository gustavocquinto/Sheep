from core.autoload import AutomationController, Logger, Asserts
from selenium.webdriver.common.by import By
from config.settings import *
from utils.data_provider import DataProvider
from validators.textBox_validator import TextBoxValidator


class TextBox():
    def __init__(self):
        self.cmd = AutomationController()
        self.data = DataProvider()
        return None
    
    def runner(self):
        self.cmd.acessaSite("https://demoqa.com/text-box")
        self.preenche_campos_corretamente()
        return None
    
    def preenche_campos_corretamente(self):

        self.pessoa = self.data.Pessoa()

        self.cmd.buscar_elemento("userName", "id").preencher(self.pessoa.nome)
        self.pessoa.nome = "Name:" + self.pessoa.nome #Melhorar

        self.cmd.buscar_elemento("userEmail", "id").preencher(self.pessoa.email)
        self.pessoa.email = "Email:" + self.pessoa.email

        self.cmd.buscar_elemento("currentAddress", "id").preencher(self.pessoa.endereco)
        pessoa_endereco = "Current Address :" + self.pessoa.endereco

        self.cmd.buscar_elemento("permanentAddress", "id").preencher(self.pessoa.endereco)
        pessoa_endereco2 = "Permananet Address :" + self.pessoa.endereco

        self.cmd.buscar_elemento("submit", "id").clicar()

        self.dados = [self.pessoa.nome, self.pessoa.email, pessoa_endereco, pessoa_endereco2]

        TextBoxValidator(self.cmd).validar_preenchimento(self.dados)

        return None