from loguru import logger

from config import LOGFILE
logger.remove()
logger.add(LOGFILE,
           format='{time:YYYY-MM-DD HH:mm:ss} | {level} - {message} (function = {function})')