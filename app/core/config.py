import os
from typing import List
from pydantic import BaseModel, BaseSettings
import dotenv


dotenv.load_dotenv()


class Server(BaseSettings):
    TITLE: str = "<Project Title>"
    HOST: str = "0.0.0.0"
    PORT: str = "8000"
    ORIGINS: List[str] = [
        "http://localhost:3000",
    ]


class Database(BaseSettings):
    DATABASE_URI: str = (
        os.environ.get("DATABASE_URL").replace("postgres://", "postgresql://")
        or "sqlite:///./sql_app.db"
    )

    class Config:
        env_file: str = ".env"


class LogConfig(BaseModel):
    LOGGER_NAME: str = "main"
    LOG_FORMAT: str = "%(levelprefix)s | %(asctime)s | %(message)s"
    LOG_LEVEL: str = "DEBUG"

    version = 1
    disable_existing_loggers = False
    formatters = {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    }
    handlers = {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
    }
    loggers = {
        "main": {"handlers": ["default"], "level": LOG_LEVEL},
    }


server = Server()
db = Database()
logger = LogConfig()
