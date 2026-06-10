import sys
from loguru import logger

logger.remove()

logger.add(
    sys.stdout,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | <cyan>{name}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    level="INFO"
)

logger.add(
    "logs/app_{time:YYYY-MM-DD}.log",
    rotation="daily",
    retention="10 days", 
    compression="zip",      
    enqueue=True,             
    level="INFO"
)
