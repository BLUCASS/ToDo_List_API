from sqlalchemy import create_engine, String, Integer, Boolean, Column
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///data.db')
Base = declarative_base()

class ToDo(Base):
    __tablename__ = 'to_do'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    complete = Column(Boolean)

Base.metadata.create_all(bind=engine)