import datetime


def logger(level, msg, logger):
    date  = datetime.datetime.now()
    with open(f'./{logger}.log', 'a') as logger:
        logger.write(f'\n [{level}] {msg} ---- {date}'.format())


def critical(msg):
    date  = datetime.datetime.now()
    with open('./logger.log', 'a') as logger:
        logger.write(f'\n [CRITICAL] {msg} ---- {date}'.format())
        

def error(msg):
    date  = datetime.datetime.now()
    with open('./logger.log', 'a') as logger:
        logger.write(f'\n [ERROR] {msg} ---- {date}'.format())
        
        
def warning(msg):
    date  = datetime.datetime.now()
    with open('./logger.log', 'a') as logger:
        logger.write(f'\n [WARNING] {msg} ---- {date}'.format())
        
        

def info(msg):
    date  = datetime.datetime.now()
    with open('./logger.log', 'a') as logger:
        logger.write(f'\n [INFO] {msg} ---- {date}'.format())
        
        
        
def debug(msg):
    date  = datetime.datetime.now()
    with open('./logger.log', 'a') as logger:
        logger.write(f'\n [DEBUG] {msg} ---- {date}'.format())