from singleton_class import Logger

logger = Logger();
logger2 = Logger();


def division():
    try:
        num_1 = int(input('Enter numerator: '))
        num_2 = int(input('Enter denominator: '))
        
    except ValueError as err:
        logger.log("ERROR", err)
        raise("Enter an Integer")
    
    else:
        try:
            calc = num_1 / num_2
            
        except ZeroDivisionError as err:
            logger.log('ERROR', err)
            raise("Can't divide number by zero")  
    
            
    return calc
        
print(logger == logger2)
division()

