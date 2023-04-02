import sys
import loguru

logger = loguru.logger
logger.remove()
logger.add(sys.stdout, format="{time} - {level} - {message} ", level="INFO")
