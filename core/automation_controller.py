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

        elif seletor_tipo == 'class_name':
            self.elemento = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, elemento)))
        elif seletor_tipo == 'tag_name':
            self.elemento = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, elemento)))

        #Certifico que estou retornando elemento visível
        self.navegador.execute_script("arguments[0].scrollIntoView();", self.elemento)

        return self
    
    @ExceptionHandler.trata_erros
    def texto(self):
        return self.elemento.text
    
    @ExceptionHandler.trata_erros
    def buscar_elementos(self, elemento='SecondName', seletor='id'):
        Logger().info_log(f"Buscando múltiplos elementos {elemento}, com seletor tipo: {seletor}...")

        seletor = seletor.lower()
        if seletor == 'tag_name':
            self.elementos = self.elemento.find_elements(By.TAG_NAME, elemento)
        elif seletor == 'css_selector':
            self.elementos = self.elemento.find_elements(By.CSS_SELECTOR, elemento)
            
        return self
    
    @ExceptionHandler.trata_erros
    def preencher(self, string="texto"):
        Logger().info_log(f"Preenchendo campo com string: {string}")
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
    
    def get_atributo_valor(self):
        
        tag = self.elemento.tag_name.lower()
        if tag in ['input', 'textarea', 'select']:
            return self.elemento.get_attribute('value')
        else:
            return self.elemento.text
        
    @ExceptionHandler.trata_erros    
    def buscar_feedback(self, elemento='Pop-up sucess', seletor='id'):
        self.elemento = self.buscar_elemento(elemento, seletor)
        if (self.elemento):
            Logger().info_log('Elemento de feedback encontrado com sucesso')
            return self
        else:
            return False
        
    def is_required(self):
        if (self.elemento.get_attribute('required')):
            return True
        