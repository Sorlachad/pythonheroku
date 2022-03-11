import logging
from types import MethodType




def writeLog(name,levelname,filename,text):
    logger = logging.getLogger(name)
    logger.setLevel(levelname)
    formatter=logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')

    file_handler = logging.FileHandler(f'{filename}.log')
    file_handler.setFormatter(formatter)
    if (logger.hasHandlers()):
        logger.handlers.clear()
    logger.addHandler(file_handler)

    if levelname==logging.WARNING:
        logger.warning(text)
    if levelname==logging.DEBUG:
        logger.debug(text)
    if levelname==logging.ERROR:
        logger.error(text)
    if levelname==logging.INFO:
        logger.info(text)
    if levelname==logging.CRITICAL:
        logger.critical(text)
    