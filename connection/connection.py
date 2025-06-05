import os.path
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

DATABASE_NAME = "blog.db"
PROJECT_PATH = os.path.dirname(os.path.abspath(__name__))
DATABASE_FOLDER_PATH = PROJECT_PATH + "/database"
DATABASE_PATH = f"{DATABASE_FOLDER_PATH}/{DATABASE_NAME}"
DATABASE_URL = f"sqlite:///{DATABASE_PATH}"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    echo=True,
)

SessionLocal = Session(
    bind=engine,
    autocommit=False,
    autoflush=False
)


def get_database():
    db = SessionLocal
    try:
        yield db
    finally:
        db.close()
