import logging

def Logger(set_level,text):
    logger=logging.getLogger('__name__')
    if(set_level=="debug"):
        logging.basicConfig(filename="LogFile/logger.log",level=logging.DEBUG,format='%(levelname)s :%(funcName)s : %(asctime)s : %(name)s : %(message)s') 
        logger.debug(text)
    elif(set_level=="info"):
        logging.basicConfig(filename="LogFile/logger.log",level=logging.INFO,format='%(levelname)s :%(funcName)s : %(asctime)s : %(name)s : %(message)s') 
        logger.info(text)
    elif(set_level=="error"):
        logging.basicConfig(filename="LogFile/logger.log",level=logging.ERROR,format='%(levelname)s :%(funcName)s : %(asctime)s : %(name)s : %(message)s') 
        logger.error(text)
    elif(set_level=="warning"):
        logging.basicConfig(filename="LogFile/logger.log",level=logging.WARNING,format='%(levelname)s :%(funcName)s : %(asctime)s : %(name)s : %(message)s') 
        logger.warning(text)
    else:
        print("do noting")
