from sqlalchemy import create_engine
from app.models import Base
import data

def start_db():
    engine = create_engine(f'mysql+pymysql://{data.USERNAME}:{data.PASSWORD}@{data.HOST}/{data.DBNAME}', echo=True, future=True)

    Base.metadata.create_all(engine)