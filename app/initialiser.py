import logging

from app.database import SessionLocal, initialise


logger = logging.getLogger("main")


def init() -> None:
    db = SessionLocal()
    initialise(db)


def main() -> None:
    logger.info("Initialising")
    init()


if __name__ == "__main__":
    main()
