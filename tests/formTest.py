from core.autoload import AutomationController, Logger, Asserts
from selenium.webdriver.common.by import By
from config.settings import *
from utils.data_provider import DataProvider
from validators.form_validator import formValidator

from time import *
import random
class FormTest:
    def __init__(self):
        self.cmd = AutomationController()
        self.data_provider = DataProvider()
        self.dados = []
        self.cmd.acessaSite(url_app)

    def runner(self):
        Logger().info_log(f"Executando classe de teste: {self.__class__.__name__}")

        self.test_preencher_formulario_corretamente()
        self.campos_obrigatorios()

    def test_preencher_formulario_corretamente(self):
        nome = self.test_preencher_formulario_corretamente.__qualname__
        Logger().info_log(f"Iniciando {nome}")

        self.pessoa = self.data_provider.Pessoa()
        self.empresa = self.data_provider.Empresa()

        self.cmd.buscar_elemento(f"firstName", "id").preencher(f"{self.pessoa.nome}")
        
        self.cmd.buscar_elemento("lastName", "id").preencher(f"{self.pessoa.sobrenome}")

        self.cmd.buscar_elemento("userEmail", "id").preencher(f"{self.pessoa.email}")

        #Genêro aleatório
        randomico = random.randint(1, 3)
        self.cmd.buscar_elemento(f'label[for="gender-radio-{randomico}"]', "css_selector").clicar()
        genero = self.cmd.buscar_elemento(f'label[for="gender-radio-{randomico}"]', "css_selector").get_atributo_valor()

        self.cmd.buscar_elemento(f"userNumber", "id").preencher(f"{self.pessoa.telefone}")

        self.cmd.buscar_elemento(f"dateOfBirthInput", "id").clicar()
        self.cmd.buscar_elemento(f'react-datepicker__day--001', 'class_name').clicar()
        self.cmd.buscar_elemento(f"dateOfBirthInput", "id").get_atributo_valor()

        self.cmd.buscar_elemento(f"subjectsInput", "id").preencher(f"Computer Science").teclaEnter()

        randomico = randomico
        self.cmd.buscar_elemento(f'label[for="hobbies-checkbox-{randomico}"]', "css_selector").clicar()
        hobbies = self.cmd.buscar_elemento(f'label[for="hobbies-checkbox-{randomico}"]', "css_selector").get_atributo_valor()

        self.cmd.buscar_elemento(f'currentAddress', 'id').preencher(f'{self.empresa.endereco}')

        self.state_options = ['NCR']
        randomico = random.randint(0, len(self.state_options) - 1)
        self.state = self.state_options[randomico]
        self.state_input = self.cmd.buscar_elemento(f'state', 'id')
        self.state_input.clicar()
        self.cmd.buscar_elemento('react-select-3-input', 'id').preencher(f'{self.state}').teclaEnter()

        self.city_options = ['Delhi', 'Gurgaon', 'Noida']
        randomico = random.randint(0, len(self.city_options) - 1)
        self.city = self.city_options[randomico]
        self.cmd.buscar_elemento('react-select-4-input', 'id').preencher(f'{self.city}').teclaEnter()
    
        self.cmd.buscar_elemento('submit', 'id').clicar()

        self.nome_completo = self.pessoa.nome + " " + self.pessoa.sobrenome
        self.city_state = self.state + " " + self.city
        print("ESTADO: " + self.city_state)
        self.dados_tabela = [self.nome_completo, self.pessoa.email, genero, self.pessoa.telefone, 'Date of birth', 'Computer Science', hobbies, '', self.empresa.endereco, self.city_state]

        formValidator(self.cmd).validar_preenchimento_formulario(self.dados_tabela)
        self.cmd.atualizar_pagina()

    def test_campos_obrigatorios(self):
        self.cmd.buscar_elemento('submit', 'id').clicar()

        Logger().info_log(self.cmd.buscar_elemento(f"firstName", "id").is_required() )


    def test_preenchimento_incorreto(self):
        self.cmd.buscar_elemento(f"firstName", "id").preencher(f"123")
        self.cmd.buscar_elemento(f"lastName", "id").preencher(f"456")

        return None