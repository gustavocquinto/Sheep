import logging
from config.settings import debug_development, debug_log_path
from datetime import datetime

class Logger():

    def __init__(self):
        log_dir = debug_log_path
        date = datetime.now()
        log_date = f"_{date.day}_{date.month}_{date.year}_{date.hour}-{date.minute}-{date.second}"

        if debug_development is True:
            logging.basicConfig(filename=f'{log_dir}debugging{log_date}.log', level=logging.DEBUG)
        else:
            logging.basicConfig(level=logging.INFO)

    @staticmethod 
    def info_log(mensagem):
        print()
        logging.info(f"{mensagem} \n")

    @staticmethod
    def error_log(mensagem):
        print()
        logging.error(f"{mensagem} \n")

    @staticmethod
    def warning_log(mensagem):
        print()
        logging.warning(f"{mensagem} \n")