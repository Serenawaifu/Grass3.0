from loguru import logger

def configure_logging():
    logger.add("bot.log", rotation="500 MB", retention="1 week", level="INFO")
