import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the absolute path for the database file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "../../db/port_app.db")
SQL_ALCHEMY_DATABSE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(SQL_ALCHEMY_DATABSE_URL, connect_args={
                       'check_same_thread': False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
