from core.autoload import AutomationController
from selenium.webdriver.common.by import By
from core.asserts_controller import Asserts

class formValidator():
    def __init__(self, automationController: AutomationController):
        self.cmd = automationController
        self.asserts = Asserts()

    def validar_preenchimento_formulario(self, dados):
        
        feedback_modal = self.cmd.buscar_feedback('modal-content', 'class_name')
        div_tabela = feedback_modal.buscar_elemento('table-responsive', 'class_name')
        tabela = div_tabela.buscar_elemento('table', 'tag_name')
        tabela_body = tabela.buscar_elemento('tbody', 'tag_name')
        linhas_tabela = tabela_body.buscar_elementos('tr', 'tag_name').elementos

        for i, linha in enumerate(linhas_tabela):
            colunas = linha.find_elements(By.TAG_NAME, 'td')
            coluna = colunas[1].text
            self.asserts.checar(dados[i], coluna)

        self.asserts.relatorio_asserts(self.validar_preenchimento_formulario.__qualname__)

    def validar_campos_obrigatorios(self):

        return None
    
    def validar_preenchimento_incorreto(self):

        return None