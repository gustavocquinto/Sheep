from selenium.common.exceptions import *
from colorama import init, Fore, Style

class ExceptionHandler():

    @staticmethod
    def printaErros(mensagem):
         
         print(f"{Fore.RED}[ERRO]: {mensagem} {Style.RESET_ALL}")

    @staticmethod
    def trata_erros(func):
        def wrapper(*args, **kwargs):
            nome_funcao = func.__name__
            try:
                return func(*args, **kwargs)
            
            except (NoSuchElementException, TimeoutException) as e:
                ExceptionHandler.printaErros(f"Elemento não encontrado ou tempo excedido, função: {nome_funcao}, exception: \n")
                print(e)
                exit()
                
            except ElementClickInterceptedException as e:
                ExceptionHandler.printaErros(f"Elemento interceptado, não foi possivel clicar. Outro elemento receberia o click \n")
                print(e)
            ##except Exception as e:
                ##print(f"[ERRO] Função {nome_funcao} : {e}")
            
        return wrapper
    

    