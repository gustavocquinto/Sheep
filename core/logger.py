import logging
from config.settings import debug_development, debug_log_path

class Logger():

    def __init__(self):
        if debug_development is True:
            logging.basicConfig(filename='debugging.log', level=logging.DEBUG)
        else:
            logging.basicConfig(level=logging.INFO)
    
    def info_log(self, mensagem):
        logging.info(mensagem)