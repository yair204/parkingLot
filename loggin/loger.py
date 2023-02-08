import logging

logger = logging.getLogger("log")
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s>>>>%(levelname)s>>>>%(message)s")
handler = logging.FileHandler("parking_lot.log")
handler.setFormatter(formatter)
logger.addHandler(handler)
