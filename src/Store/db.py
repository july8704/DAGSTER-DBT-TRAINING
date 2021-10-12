from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class db_manager:

    conn_str = "postgresql://postgres:Nike1604_@186.83.193.210:5432/project_hobby_store"
    engine = create_engine(conn_str)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Mapeo entre clases y tablas
    Base = declarative_base()





