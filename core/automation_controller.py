import selenium
from core.webdriver_service import WebDriverService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from core.exception_handler import ExceptionHandler
from core.logger import Logger

class AutomationController:

    def __init__(self):
        self.webdriver = WebDriverService()
        self.logger = Logger()

        self.navegador = self.webdriver.driver
        
        self.wait = self.webdriver.wait

    @ExceptionHandler.trata_erros
    def buscaElemento(self, elemento='firstName', seletor='id'):
        self.logger.info_log(f"Buscando elemento {elemento}, com seletor tipo: {seletor}...")
        seletor_tipo = seletor.lower()
        
        if seletor_tipo == 'xpath':
            self.elemento = self.wait.until(EC.presence_of_element_located((By.XPATH, elemento)))

        elif seletor_tipo == 'id':
            self.elemento = self.wait.until(EC.presence_of_element_located((By.ID, elemento)))

        elif seletor_tipo == 'css_selector':
            self.elemento = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, elemento)))

        #Certifico que estou retornando elemento visível
        self.navegador.execute_script("arguments[0].scrollIntoView();", self.elemento)

        return self
    
    @ExceptionHandler.trata_erros
    def preencher(self, string="texto"):
        self.elemento.send_keys(string)
        return self

    @ExceptionHandler.trata_erros
    def clicar(self):
        self.elemento.click()

    @ExceptionHandler.trata_erros
    def teclaEnter(self):
        self.elemento.send_keys(Keys.ENTER)

    @ExceptionHandler.trata_erros
    def acessaSite(self, url):
        self.navegador.get(url)

        return self

