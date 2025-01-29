import logging

logging.basicConfig(
    filename='app.log',
    filemode='a',
    level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

logger = logging.getLogger(__name__)

def divide(a, b):
    try:
        logger.info(f"Division operation started, dividing {a} by {b}")
        result = a / b
    except ZeroDivisionError:
        logger.critical("Cannot divide by zero")
        return None
    else:
        return result
    finally:
        logger.debug("Division operation completed")

divide(10,3)