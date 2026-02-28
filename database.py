
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url = "mysql+pymysql://root:1729@localhost:3306/fastapi?charset=utf8mb4"
engine = create_engine(db_url)
session = sessionmaker(autocommit = False, autoflush=False,bind=engine)