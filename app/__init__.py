from logging.config import dictConfig

from app.core import config


dictConfig(config.logger.dict())
