import logging

class Logger():
    def __init__(self):
        logging.basicConfig(level=logging.INFO, filename='logs.log')

    def debug(self, message:str)->None:
        logging.debug(message)

    def info(self, message:str)->None:
        logging.info(message)

    def warning(self, message:str)->None:
        logging.warning(message)

    def error(self, message:str)->None:
        logging.error(message)



