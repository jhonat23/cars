from sqlalchemy import create_engine
from models import Base, Seller, Car
from sqlalchemy.orm import Session
import data as data

engine = create_engine(f'mysql+pymysql://{data.USERNAME}:{data.PASSWORD}@{data.HOST}/{data.DBNAME}', echo=True, future=True)

Base.metadata.create_all(engine)

# operations
def get_seller(name: str):
    with Session(engine) as session:
        result = session.query(Seller).filter_by(name=name).all()
        if result:
            return result
        else:
            return False

def get_cars(name: str):
    with Session(engine) as session:
        result = session.query(Car).filter_by(name=name).all()
        if result:
            return result
        else:
            return False

if __name__ == '__main__':
    seller = get_seller('Todo Autos')
    cars = get_cars('renault')
    print(seller)
    cars = [print(car) for car in cars]