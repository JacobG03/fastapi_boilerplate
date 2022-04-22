import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core import config


logger = logging.getLogger("main")
database_name = "postgres"

if database_name in config.db.DATABASE_URI:
    engine = create_engine(config.db.DATABASE_URI, pool_pre_ping=True)
    logger.info(f"Connected to {database_name} database.")
else:
    engine = create_engine(
        config.db.DATABASE_URI, connect_args={"check_same_thread": False}
    )
    logger.info("Created a SQLite database.")
    logger.info("Connected to the SQLite database.")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
