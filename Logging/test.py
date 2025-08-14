from logger import logger


def add(a, b):
    logger.debug("addition operation is taking place")
    return a + b


logger.debug("addition function is called")
add(10, 15)
logger.debug("addition done")
