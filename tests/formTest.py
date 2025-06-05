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
        self.formValidator = formValidator(self.cmd)
        self.dados = []
        self.cmd.acessaSite(url_app)

    def preencher_formulario_corretamente(self):
        nome = self.preencher_formulario_corretamente.__qualname__
        Logger().info_log(f"Iniciando teste...{nome}")

        self.pessoa = self.data_provider.Pessoa()
        self.empresa = self.data_provider.Empresa()

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

        self.cmd.buscar_elemento(f'currentAddress', 'id').preencher(f'{self.empresa.endereco}')

        self.state_options = ['NCR', 'Uttar Pradesh', 'Haryana', 'Rajasthan']
        randomico = random.randint(0, len(self.state_options) - 1)
        self.state = self.state_options[randomico]
        self.state_input = self.cmd.buscar_elemento(f'state', 'id')
        self.state_input.clicar()
        self.cmd.buscar_elemento('react-select-3-input', 'id').preencher(f'{self.state}').teclaEnter()

        self.city_options = ['Delhi', 'Gurgaon', 'Noida']
        randomico = random.randint(0, len(self.city_options) - 1)
        self.city = self.city_options[randomico]
        self.cmd.buscar_elemento('react-select-4-input', 'id').preencher(f'{self.city}')
    
        self.cmd.buscar_elemento('submit', 'id').clicar()

        feedback_modal = self.cmd.buscar_feedback('modal-content', 'class_name')
        div_tabela = feedback_modal.buscar_elemento('table-responsive', 'class_name')
        tabela = div_tabela.buscar_elemento('table', 'tag_name')
        tabela_body = tabela.buscar_elemento('tbody', 'tag_name')
        linhas_tabela = tabela_body.buscar_elementos('tr', 'tag_name').elementos

        for i, linha in enumerate(linhas_tabela):
            colunas = linha.find_elements(By.TAG_NAME, 'td')
            if (i == 0):
                self.nome_completo = self.pessoa.nome + ' ' + self.pessoa.sobrenome
                Asserts().checar(self.nome_completo, colunas[1].text)
            


       # self.formValidator.validar_preenchimento_formulario(self.dados)
        sleep(10)


