import selenium
from WebDriverService import WebDriverService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from ExceptionHandler import ExceptionHandler


class AutomationController:

    def __init__(self):
        self.webdriver = WebDriverService()

        self.navegador = self.webdriver.driver
        
        self.wait = self.webdriver.wait

    @ExceptionHandler.trata_erros
    def buscaElemento(self, elemento='firstName', seletor='id'):
        seletor_tipo = seletor.lower()
        if seletor_tipo == 'xpath':
            self.elemento = self.wait.until(EC.presence_of_element_located((By.XPATH, elemento)))

        elif seletor_tipo == 'id':
            self.elemento = self.wait.until(EC.presence_of_element_located((By.ID, elemento)))

        elif seletor_tipo == 'css_selector':
            self.elemento = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, elemento)))

        return self
    
    @ExceptionHandler.trata_erros
    def preencher(self, string="texto"):
        self.elemento.send_keys(string)

    @ExceptionHandler.trata_erros
    def clicar(self):
        self.elemento.click()

    @ExceptionHandler.trata_erros
    def acessaSite(self, url):
        self.navegador.get(url)

        return self

