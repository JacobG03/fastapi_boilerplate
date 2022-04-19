import logging
from sqlalchemy.orm import Session

from app.database import Base, engine


logger = logging.getLogger('main')

def initialise(db: Session) -> None:
    Base.metadata.create_all(bind=engine)
    logger.info('Database Tables created.')
