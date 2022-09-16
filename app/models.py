from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

#models

class Seller(Base):
    __tablename__ = 'sellers'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)

    cars = relationship('Car', back_populates='seller')

    def __str__(self):
        return {'name': f'{self.name}'}

class Car(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    brand = Column(String(50), nullable=False)
    model = Column(Integer, nullable=False)
    cv = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    seller_id = Column(Integer, ForeignKey('sellers.id'))

    seller = relationship('Seller', back_populates='cars')
