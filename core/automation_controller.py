from core.autoload import Asserts, Logger, ExceptionHandler, WebDriverService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


class AutomationController:

    def __init__(self):
        self.webdriver = WebDriverService()
        self.asserts = Asserts()

        self.navegador = self.webdriver.driver
        
        self.wait = self.webdriver.wait

        

    @ExceptionHandler.trata_erros
    def buscar_elemento(self, elemento='firstName', seletor='id'):
        Logger().info_log(f"Buscando elemento {elemento}, com seletor tipo: {seletor}...")
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
    
    @ExceptionHandler.trata_erros
    def validar(self, valor_esperado):
        valor_salvo = self.get_element_value(self.elemento)
        self.asserts.checar(valor_esperado, valor_salvo)

    def get_element_value(self, elemento):
        
        tag = elemento.tag_name.lower()
        if tag in ['input', 'textarea', 'select']:
            return elemento.get_attribute('value')
        else:
            return elemento.text