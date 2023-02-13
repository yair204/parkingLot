import logging
import logging.handlers


LOG_FILENAME = 'parking_lot.log'
handler = logging.handlers.RotatingFileHandler(
    LOG_FILENAME,
    maxBytes = 1024*10,
    backupCount=5,
)

def namer(name):
    return name.replace(".log", "") + ".log"

logger = logging.getLogger("log")
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s>>>>%(levelname)s>>>>%(message)s")
handler.setFormatter(formatter)
handler.namer = namer
logger.addHandler(handler)

def logger_func(func):
    def inner_func(*args, **kwargs):
        try:
            tmp = func(*args, **kwargs)
            logger.info(f'function->{func.__name__}()-> succeeded')
            return tmp
        except Exception:
            logger.info(f'function->{func.__name__}()-> she did not succeed')
            raise ValueError
    return inner_func
