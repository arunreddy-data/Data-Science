import logging

## logging Setting
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s-%(name)s-%(levelname)s-%(message)s",
    datefmt="%Y-%m-%d %H:%M%S",
    handlers=[logging.FileHandler("app1.log"), logging.StreamHandler()],
)
logger = logging.getLogger("ArthmeticApp")


def add(a, b):
    result = a + b
    logger.debug(f"Adding '{a} + {b}={result}")
    return result


def substract(a, b):
    result = a - b
    logger.debug(f"substracting '{a} - {b}={result}")
    return result


def multiply(a, b):
    result = a * b
    logger.debug(f"multiplying '{a} * {b}={result}")
    return result


def divide(a, b):
    try:
        result = a / b
        logger.debug(f"dividing '{a} * {b}={result}")
        return result
    except ZeroDivisionError as e:
        logger.error("Division Error By Zero")
        return None


add(10, 20)
substract(15, 20)
multiply(10, 2)
divide(20, 0)
