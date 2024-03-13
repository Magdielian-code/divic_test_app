import json
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

def add_data(model, data):
    """ Add this data to the table in database """
    db_path = "database.db"
    engine = create_engine(f"sqlite:///{db_path}")
    
    Base = declarative_base(bind=engine)
    
    class MyModel(Base):
        __tablename__ = model.__tablename__
        id = Column(Integer, primary_key=True)
        # Add columns for your model here
        
    Base.metadata.create_all()
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    new_data = model(**data)
    session.add(new_data)
    session.commit()