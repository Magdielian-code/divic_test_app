import json
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class Model(Base):
    __tablename__ = "models"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    fields = Column(String)


def create_table(model):
    """Create table in SQLite database based on the model."""
    db_path = "database.db"
    engine = create_engine(f"sqlite:///{db_path}")
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_model = Model(name=model["name"], fields=json.dumps(model["fields"]))
    session.add(new_model)
    session.commit()
    session.close()

    return
