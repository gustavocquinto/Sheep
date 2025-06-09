from selenium.common.exceptions import *
from colorama import init, Fore, Style
from core.autoload import Logger
from urllib3.exceptions import MaxRetryError, NewConnectionError

class ExceptionHandler():

    
    @staticmethod
    def trata_erros(func):
        def wrapper(*args, **kwargs):
            nome_funcao = func.__name__
            try:
                return func(*args, **kwargs)
            
            except (NoSuchElementException, TimeoutException) as e:
                Logger.error_log(f"Elemento não encontrado ou tempo excedido, função: {nome_funcao}")
                print(e)
                exit()
                
            except ElementClickInterceptedException as e:
                Logger.error_log(f"Elemento interceptado, não foi possivel clicar. Outro elemento receberia o click. Função: {nome_funcao}")
                print(e)

            except KeyboardInterrupt as e:
                Logger.warning_log(f"Execução de script interrompida pelo teclado.Função: {nome_funcao}")
                print(e)
                exit()
            
            except NoSuchWindowException as e:
                Logger.error_log(f"Não foi possivel continuar. Verifique se a janela do navegador foi fechada. Função: {nome_funcao}")
                exit()

            except AttributeError as e:
                Logger.error_log(f"Não foi possível encontrar o atributo informado Função: {nome_funcao}")
                print(e)

            except (ConnectionError, ConnectionAbortedError, ConnectionRefusedError) as e:
                Logger.error_log(f"Conexão com o driver do navegador negada ou interrompida. Parece que há um problema ao solicitar ações ao navegador. Função: {nome_funcao}")
                print(e)
                exit()

            except MaxRetryError as e:
                Logger.error_log(f"Tentativas Excedidas: Não foi possivel realizar a conexão com o driver do navegador. Por favor, confirme as configurações e disponibilidade do driver. Função: {nome_funcao}")
                exit()

            except NewConnectionError as e:
                Logger.error_log(f" Não foi possivel realizar a conexão com o driver do navegador. Por favor, confirme as configurações e disponibilidade do driver. Função: {nome_funcao}")
                exit()

            except Exception as e:
                Logger.error_log(f"A execução foi interrompida. Não foi possível identificar uma exceção respectiva para tratamento. Função: {nome_funcao}")
                print(e)
            ##except Exception as e:
                ##print(f"[ERRO] Função {nome_funcao} : {e}")
            
        return wrapper
    

    