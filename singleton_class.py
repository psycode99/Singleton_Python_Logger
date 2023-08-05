import datetime


class Logger(object):
    
    def __init__(self) -> None:
        self.filename = "pyLogger"
        
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Logger, cls).__new__(cls)
        return cls.instance
    
    
    def log(self, level, msg):
        date = datetime.datetime.now()
        with open(f"{self.filename}.log", 'a') as logger:
            logger.write(f"[{level}] ---- {msg} ---- {date}\n")
            
    