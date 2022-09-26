from sqlalchemy import create_engine
from app.models import Base, Seller, Car
from sqlalchemy.orm import Session
import app.data as data

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
    
def get_all_cars():
    with Session(engine) as session:
        result = session.query(Car).all()
        if result:
            return result
        else:
            return False

if __name__ == '__main__':
    seller = get_seller('Todo Autos')
    cars = get_cars('kia')
    print(seller)
    cars = [print(car) for car in cars]

    # all = get_all_cars()
    # all = [print(car) for car in all]